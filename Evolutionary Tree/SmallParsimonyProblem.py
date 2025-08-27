import math
from collections import defaultdict

ALPHABET = "ACGT"

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def parse_input(lines):
    n = int(lines[0].strip())
    labels = {}
    children = defaultdict(list)
    nodes = set()
    leaf_counter = 0  # Start from 0 for leaf IDs
    
    # First pass: identify all nodes and create leaf nodes
    for line in lines[1:]:
        u, v = line.strip().split("->")
        u = int(u)
        nodes.add(u)
        
        if all(c in ALPHABET for c in v):  # leaf with DNA string
            labels[leaf_counter] = v
            children[u].append(leaf_counter)
            nodes.add(leaf_counter)
            leaf_counter += 1
        else:  # edge between internal nodes
            v = int(v)
            children[u].append(v)
            nodes.add(v)
    
    return n, labels, children, nodes

def small_parsimony_on_column(children, labels, nodes, col):
    # Initialization
    Tag = {v: 0 for v in nodes}
    S = {v: {k: math.inf for k in ALPHABET} for v in nodes}

    # Initialize leaf nodes
    for v in nodes:
        if v in labels:  # leaf
            Tag[v] = 1
            for k in ALPHABET:
                if labels[v][col] == k:
                    S[v][k] = 0
                else:
                    S[v][k] = math.inf

    # Process internal nodes using ripe node algorithm
    changed = True
    while changed:
        changed = False
        for v in nodes:
            if Tag[v] == 0 and v in children and len(children[v]) == 2:
                left, right = children[v]
                if Tag[left] == 1 and Tag[right] == 1:
                    for k in ALPHABET:
                        left_cost = min(S[left][i] + (0 if i == k else 1) for i in ALPHABET)
                        right_cost = min(S[right][j] + (0 if j == k else 1) for j in ALPHABET)
                        S[v][k] = left_cost + right_cost
                    Tag[v] = 1
                    changed = True

    # Find the root (highest numbered node that's internal)
    root = max(v for v in nodes if v not in labels)
    return min(S[root].values()), S, root

def traceback(children, labels, nodes, S_tables, roots, m):
    # reconstruct sequences by column
    node_strings = {v: [""] * m for v in nodes}

    for col in range(m):
        S = S_tables[col]
        root = roots[col]
        
        # pick min at root (choose lexicographically first in case of ties)
        min_cost = min(S[root].values())
        root_char = None
        for k in ALPHABET:  # ALPHABET = "ACGT" so this gives lexicographic order
            if S[root][k] == min_cost:
                root_char = k
                break
        assignment = {root: root_char}

        # recursive traceback
        def assign(v):
            if v not in children or len(children[v]) == 0: 
                return
            parent_char = assignment[v]
            for child in children[v]:
                if child in labels:  # leaf node - use actual character
                    assignment[child] = labels[child][col]
                else:  # internal node - find optimal (lexicographically first in ties)
                    best_char = None
                    best_val = math.inf
                    for k in ALPHABET:  # Process in ACGT order for consistent tie-breaking
                        cost = S[child][k] + (0 if k == parent_char else 1)
                        if cost < best_val:
                            best_val = cost
                            best_char = k
                    assignment[child] = best_char
                assign(child)

        assign(root)
        
        # fill this column
        for v in nodes:
            if v in assignment:
                node_strings[v][col] = assignment[v]

    # join characters to form sequences
    for v in nodes:
        node_strings[v] = "".join(node_strings[v])
    return node_strings

def small_parsimony(lines):
    n, labels, children, nodes = parse_input(lines)
    
    if not labels:
        return ["0"]
        
    m = len(next(iter(labels.values())))
    total_score = 0
    S_tables = {}
    roots = {}
    
    # Debug: print tree structure
    # print(f"Debug - Labels: {labels}")
    # print(f"Debug - Children: {dict(children)}")
    # print(f"Debug - Nodes: {nodes}")
    
    for col in range(m):
        score, S, root = small_parsimony_on_column(children, labels, nodes, col)
        total_score += score
        S_tables[col] = S
        roots[col] = root
    
    node_strings = traceback(children, labels, nodes, S_tables, roots, m)
    
    # print(f"Debug - Node strings: {node_strings}")

    # build adjacency list with Hamming distances
    edges = []
    for u in children:
        for v in children[u]:
            if u in node_strings and v in node_strings:
                dist = hamming(node_strings[u], node_strings[v])
                edges.append(f"{node_strings[u]}->{node_strings[v]}:{dist}")
                edges.append(f"{node_strings[v]}->{node_strings[u]}:{dist}")

    return [str(total_score)] + edges

with open('C:/Users/Matthew/Downloads/dataset_30291_9 (2).txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
result = small_parsimony(lines)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for line in result:
        print(line)
        f.write(f"{line}\n")