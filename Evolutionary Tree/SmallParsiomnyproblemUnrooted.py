import math
from collections import defaultdict

ALPHABET = "ACGT"

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def parse_unrooted_input(lines):
    """Parse unrooted tree where leaves are connected to internal nodes"""
    n = int(lines[0].strip())
    labels = {}
    adjacency = defaultdict(set)
    nodes = set()
    
    # Track sequences we've already seen to avoid duplicates
    sequence_to_id = {}
    leaf_counter = 100  # Start leaf IDs high to avoid conflicts
    
    print("Debug: Parsing input...")
    
    for line in lines[1:]:
        u, v = line.strip().split("->")
        print(f"Processing: {u} -> {v}")
        
        # Check if u is a DNA sequence (leaf)
        if all(c in ALPHABET for c in u):
            # u is a leaf sequence, v is internal node
            leaf_seq = u
            internal_node = int(v)
            
            # Get or create leaf ID for this sequence
            if leaf_seq not in sequence_to_id:
                leaf_id = leaf_counter
                leaf_counter += 1
                sequence_to_id[leaf_seq] = leaf_id
                labels[leaf_id] = leaf_seq
                nodes.add(leaf_id)
                print(f"  Created new leaf {leaf_seq} (ID {leaf_id})")
            else:
                leaf_id = sequence_to_id[leaf_seq]
                print(f"  Using existing leaf {leaf_seq} (ID {leaf_id})")
            
            adjacency[leaf_id].add(internal_node)
            adjacency[internal_node].add(leaf_id)
            nodes.add(internal_node)
            
        # Check if v is a DNA sequence (leaf)  
        elif all(c in ALPHABET for c in v):
            # v is a leaf sequence, u is internal node
            internal_node = int(u)
            leaf_seq = v
            
            # Get or create leaf ID for this sequence
            if leaf_seq not in sequence_to_id:
                leaf_id = leaf_counter
                leaf_counter += 1
                sequence_to_id[leaf_seq] = leaf_id
                labels[leaf_id] = leaf_seq
                nodes.add(leaf_id)
                print(f"  Created new leaf {leaf_seq} (ID {leaf_id})")
            else:
                leaf_id = sequence_to_id[leaf_seq]
                print(f"  Using existing leaf {leaf_seq} (ID {leaf_id})")
            
            adjacency[internal_node].add(leaf_id)
            adjacency[leaf_id].add(internal_node)
            nodes.add(internal_node)
            
        else:
            # Both are internal nodes
            u, v = int(u), int(v)
            adjacency[u].add(v)
            adjacency[v].add(u)
            nodes.add(u)
            nodes.add(v)
    
    print(f"Debug: Final tree structure:")
    print(f"  Labels = {labels}")
    print(f"  Nodes = {nodes}")
    
    return n, labels, adjacency, nodes

def root_tree_at_node(adjacency, root, nodes):
    """Convert unrooted tree to rooted tree with given root"""
    children = defaultdict(list)
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in adjacency[node]:
            if neighbor != parent and neighbor not in visited:
                children[node].append(neighbor)
                dfs(neighbor, node)
    
    dfs(root, None)
    return children

def small_parsimony_column(labels, children, nodes, root, col):
    """Solve small parsimony for a single column"""
    # Initialize DP tables
    Tag = {v: 0 for v in nodes}
    S = {v: {k: math.inf for k in ALPHABET} for v in nodes}
    
    # Initialize leaves
    for v in labels:
        Tag[v] = 1
        for k in ALPHABET:
            if labels[v][col] == k:
                S[v][k] = 0
            else:
                S[v][k] = math.inf
    
    # Process internal nodes bottom-up
    changed = True
    while changed:
        changed = False
        for v in nodes:
            if Tag[v] == 0 and v in children:
                child_list = children[v]
                # Check if all children are ready
                all_children_ready = all(Tag[child] == 1 for child in child_list)
                
                if all_children_ready and len(child_list) > 0:
                    for k in ALPHABET:
                        total_cost = 0
                        for child in child_list:
                            child_cost = min(S[child][i] + (0 if i == k else 1) for i in ALPHABET)
                            total_cost += child_cost
                        S[v][k] = total_cost
                    
                    Tag[v] = 1
                    changed = True
    
    if Tag[root] == 0:
        return math.inf, {}
    
    # Find minimum cost
    root_cost = min(S[root].values())
    
    # Find all optimal assignments by trying all possible root characters
    all_assignments = []
    
    for root_char in ALPHABET:
        if S[root][root_char] == root_cost:
            assignment = {}
            
            def assign_optimal(v, parent_char=None):
                if v in labels:
                    assignment[v] = labels[v][col]
                    return
                
                if parent_char is None:
                    assignment[v] = root_char
                else:
                    # Find all characters that give optimal cost
                    optimal_chars = []
                    min_cost = math.inf
                    for k in ALPHABET:
                        cost = S[v][k]
                        if cost < min_cost:
                            min_cost = cost
                            optimal_chars = [k]
                        elif cost == min_cost:
                            optimal_chars.append(k)
                    
                    # Prefer parent character if it's optimal (no substitution)
                    if parent_char in optimal_chars:
                        assignment[v] = parent_char
                    else:
                        # Choose lexicographically smallest
                        assignment[v] = min(optimal_chars)
                
                for child in children.get(v, []):
                    assign_optimal(child, assignment[v])
            
            assign_optimal(root)
            all_assignments.append(assignment)
    
    # Choose the assignment that produces the lexicographically smallest sequences
    # when internal nodes are ordered by their final sequences
    best_assignment = None
    best_key = None
    
    for assignment in all_assignments:
        # Get internal node characters for this column
        internal_chars = []
        for v in sorted(nodes):
            if v not in labels and v in assignment:
                internal_chars.append((v, assignment[v]))
        
        # Create a key based on the characters assigned
        key = tuple(char for _, char in sorted(internal_chars))
        
        if best_key is None or key < best_key:
            best_key = key
            best_assignment = assignment
    return root_cost, best_assignment

def small_parsimony_rooted(labels, children, nodes, root):
    """Standard small parsimony for rooted tree"""
    if not labels:
        return math.inf, {}
        
    m = len(next(iter(labels.values())))
    total_score = 0
    node_strings = {v: [""] * m for v in nodes}
    
    for col in range(m):
        col_score, assignment = small_parsimony_column(labels, children, nodes, root, col)
        
        if col_score == math.inf:
            return math.inf, {}
        
        total_score += col_score
        
        # Fill this column
        for v in nodes:
            if v in assignment:
                node_strings[v][col] = assignment[v]
    
    # Join characters to form sequences
    for v in nodes:
        node_strings[v] = "".join(node_strings[v])
    
    return total_score, node_strings

def unrooted_small_parsimony(lines):
    """Solve unrooted small parsimony by trying different roots"""
    n, labels, adjacency, nodes = parse_unrooted_input(lines)
    
    if not labels:
        return ["0"]
    
    best_score = math.inf
    best_strings = {}
    best_adjacency = adjacency
    all_solutions = []
    
    # Try rooting at each internal node
    internal_nodes = [v for v in nodes if v not in labels]
    
    for root_candidate in internal_nodes:
        print(f"Debug: Trying root {root_candidate}")
        
        # Root the tree at this node
        children = root_tree_at_node(adjacency, root_candidate, nodes)
        
        # Solve rooted parsimony
        score, node_strings = small_parsimony_rooted(labels, children, nodes, root_candidate)
        
        if score < best_score:
            best_score = score
            all_solutions = [(score, node_strings, adjacency)]
        elif score == best_score:
            all_solutions.append((score, node_strings, adjacency))
    
    # Also try virtual roots on internal edges
    virtual_root_id = max(nodes) + 1
    for u in internal_nodes:
        for v in adjacency[u]:
            if v in internal_nodes and v > u:
                print(f"Debug: Trying virtual root on edge {u}-{v}")
                
                # Create modified adjacency with virtual root
                modified_adjacency = defaultdict(set)
                modified_nodes = nodes.copy()
                
                # Copy all connections except u-v
                for node in adjacency:
                    for neighbor in adjacency[node]:
                        if not ((node == u and neighbor == v) or (node == v and neighbor == u)):
                            modified_adjacency[node].add(neighbor)
                
                # Add virtual root
                modified_adjacency[virtual_root_id].add(u)
                modified_adjacency[virtual_root_id].add(v)
                modified_adjacency[u].add(virtual_root_id)
                modified_adjacency[v].add(virtual_root_id)
                modified_nodes.add(virtual_root_id)
                
                children = root_tree_at_node(modified_adjacency, virtual_root_id, modified_nodes)
                score, node_strings = small_parsimony_rooted(labels, children, modified_nodes, virtual_root_id)
                
                if score < best_score:
                    best_score = score
                    all_solutions = [(score, node_strings, modified_adjacency)]
                elif score == best_score:
                    all_solutions.append((score, node_strings, modified_adjacency))
                
                virtual_root_id += 1
    
    if best_score == math.inf:
        return ["inf"]
    
    # Among all optimal solutions, choose based on complete internal sequences
    def solution_key(sol):
        score, node_strings, adj = sol
        # Get all internal node sequences and sort them
        internal_seqs = []
        for v in sorted(nodes):
            if v not in labels and v in node_strings:
                internal_seqs.append(node_strings[v])
        internal_seqs.sort()  # Sort sequences themselves
        return tuple(internal_seqs)
    
    best_solution = min(all_solutions, key=solution_key)
    _, best_strings, best_adjacency = best_solution
    
    print(f"Debug: Best score = {best_score}")
    print(f"Debug: Best strings = {best_strings}")
    
    # Generate edges
    edges = []
    processed_pairs = set()
    
    for u in best_adjacency:
        for v in best_adjacency[u]:
            pair_key = tuple(sorted([str(u), str(v)]))
            if pair_key not in processed_pairs:
                processed_pairs.add(pair_key)
                if u in best_strings and v in best_strings:
                    dist = hamming(best_strings[u], best_strings[v])
                    edges.extend([
                        f"{best_strings[u]}->{best_strings[v]}:{dist}",
                        f"{best_strings[v]}->{best_strings[u]}:{dist}"
                    ])
    
    return [str(best_score)] + edges

with open('C:/Users/Matthew/Downloads/dataset_30291_11.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
result = unrooted_small_parsimony(lines)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for line in result:
        print(line)
        f.write(f"{line}\n")