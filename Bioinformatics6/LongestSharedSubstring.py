def TreeColoring(Tree, Colors):
    while True:
        NotDone = []
        for node in Tree.keys():
            if node not in Colors:
                NotDone.append(node)
        if not NotDone:
            break
        progress_made = False
        for node in NotDone:
            ChildColor = []
            for child in Tree[node]:
                ChildColor.append(Colors.get(child))
            if None in ChildColor:
                continue  # Skip this node, not all children are colored yet
            
            if len(set(ChildColor)) == 1:
                Colors[node] = ChildColor[0]
            else:
                Colors[node] = "purple"
            progress_made = True
        if not progress_made:
            print("No progress made - possible issue with tree structure")
            break
    return Colors

def build_suffix_tree_simple(text1, text2):
    """Build a simplified suffix tree structure using all suffixes"""
    # Combine texts with unique separators
    combined = text1 + "$" + text2 + "#"
    n1, n2 = len(text1), len(text2)
    
    # Create all suffixes
    suffixes = []
    for i in range(len(combined)):
        suffixes.append((combined[i:], i))
    
    # Build tree structure based on common prefixes
    tree = {}
    node_info = {}  # Maps node_id to (string_represented, original_positions)
    node_id = 0
    
    # Root node
    tree[node_id] = []
    node_info[node_id] = ("", [])
    root_id = node_id
    node_id += 1
    
    # Group suffixes by first character
    char_groups = {}
    for suffix, pos in suffixes:
        if suffix:
            first_char = suffix[0]
            if first_char not in char_groups:
                char_groups[first_char] = []
            char_groups[first_char].append((suffix, pos))
    
    # Build tree recursively
    def build_node(parent_id, suffix_list, common_prefix=""):
        nonlocal node_id
        
        if len(suffix_list) == 1:
            # Leaf node
            leaf_id = node_id
            node_id += 1
            tree[leaf_id] = []
            suffix, pos = suffix_list[0]
            node_info[leaf_id] = (common_prefix + suffix, [pos])
            tree[parent_id].append(leaf_id)
            return leaf_id
        
        # Find longest common prefix among all suffixes
        if not suffix_list:
            return parent_id
            
        first_suffix = suffix_list[0][0]
        lcp_len = 0
        
        while lcp_len < len(first_suffix):
            char = first_suffix[lcp_len]
            if all(lcp_len < len(s[0]) and s[0][lcp_len] == char for s in suffix_list):
                lcp_len += 1
            else:
                break
        
        if lcp_len > 0:
            # Create internal node for common prefix
            internal_id = node_id
            node_id += 1
            tree[internal_id] = []
            positions = [pos for _, pos in suffix_list]
            node_info[internal_id] = (common_prefix + first_suffix[:lcp_len], positions)
            tree[parent_id].append(internal_id)
            
            # Group remaining suffixes
            remaining_groups = {}
            for suffix, pos in suffix_list:
                remaining = suffix[lcp_len:]
                if remaining:
                    first_char = remaining[0]
                    if first_char not in remaining_groups:
                        remaining_groups[first_char] = []
                    remaining_groups[first_char].append((remaining, pos))
            
            # Recursively build subtrees
            for group in remaining_groups.values():
                build_node(internal_id, group, common_prefix + first_suffix[:lcp_len])
            
            return internal_id
        else:
            # Group by first character and build subtrees
            groups = {}
            for suffix, pos in suffix_list:
                if suffix:
                    first_char = suffix[0]
                    if first_char not in groups:
                        groups[first_char] = []
                    groups[first_char].append((suffix, pos))
            
            for group in groups.values():
                build_node(parent_id, group, common_prefix)
            
            return parent_id
    
    # Build the tree
    for char, group in char_groups.items():
        build_node(root_id, group)
    
    return tree, node_info, n1, n2

def longest_shared_substring(text1, text2):
    """Find longest shared substring using tree coloring"""
    
    # Build suffix tree
    tree, node_info, n1, n2 = build_suffix_tree_simple(text1, text2)
    
    # Color leaf nodes based on which string they come from
    colors = {}
    
    for node_id in tree:
        if not tree[node_id]:  # Leaf node
            positions = node_info[node_id][1]
            # Check which string(s) this suffix belongs to
            from_text1 = any(pos <= n1 for pos in positions)
            from_text2 = any(pos > n1 + 1 for pos in positions)  # +1 for the '$' separator
            
            if from_text1 and not from_text2:
                colors[node_id] = "red"
            elif from_text2 and not from_text1:
                colors[node_id] = "blue"
            else:
                colors[node_id] = "purple"  # Should not happen in proper suffix tree
    
    # Apply tree coloring
    colors = TreeColoring(tree, colors)
    
    # Find longest substring represented by a purple node
    longest_substring = ""
    
    for node_id, color in colors.items():
        if color == "purple":
            substring = node_info[node_id][0]
            # Remove separators and ensure it's a valid substring
            if '$' not in substring and '#' not in substring:
                if len(substring) > len(longest_substring):
                    # Verify it actually appears in both strings
                    if substring in text1 and substring in text2:
                        longest_substring = substring
    
    return longest_substring

def solve_longest_shared_substring():
    with open("C:/Users/Matthew/Downloads/dataset_30222_6.txt", 'r') as file:
        Lines = file.read().strip().split('\n')
    text1 = Lines[0]
    text2 = Lines[-1]
    
    # Also implement a simple brute force solution for comparison
    def brute_force_solution(s1, s2):
        longest = ""
        for i in range(len(s1)):
            for j in range(i + 1, len(s1) + 1):
                substr = s1[i:j]
                if substr in s2 and len(substr) > len(longest):
                    longest = substr
        return longest
    
    print("Sample Input:")
    print(text1)
    print(text2)
    print()
    
    # Use brute force for reliable result (suffix tree implementation is complex)
    result = brute_force_solution(text1, text2)
    
    print("Sample Output:")
    print(result)

'''
Sample Input:
TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA

Sample Output:
AGA
'''
solve_longest_shared_substring()