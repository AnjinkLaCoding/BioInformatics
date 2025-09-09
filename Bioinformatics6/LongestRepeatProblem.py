from collections import defaultdict

def ModifiedSuffixTrieConstruction(Text):
    Trie = {}
    
    for i in range(len(Text)):
        currentNode = Trie
        
        for j in range(i, len(Text)):
            currentSymbol = Text[j]
            
            if currentSymbol in currentNode:
                currentNode = currentNode[currentSymbol]
            else:
                newNode = {}
                currentNode[currentSymbol] = newNode
                currentNode = newNode
        
        currentNode['$END$'] = i
    
    return Trie

def get_children(node):
    if not isinstance(node, dict):
        return []
    return [k for k in node.keys() if k != '$END$']

def compress_tree(trie, text):
    def compress_node(node):
        if not isinstance(node, dict):
            return node
        
        children = get_children(node)
        
        for child_key in list(children):
            child_node = node[child_key]
            compressed_child = compress_node(child_node)
            
            child_children = get_children(compressed_child)
            
            if len(child_children) == 1 and '$END$' not in compressed_child:
                grandchild_key = child_children[0]
                grandchild = compressed_child[grandchild_key]
                
                combined_key = child_key + grandchild_key
                del node[child_key]
                node[combined_key] = grandchild
                
                return compress_node(node)
            else:
                node[child_key] = compressed_child
        
        return node
    
    return compress_node(trie)

def ModifiedSuffixTreeConstruction(Text):
    trie = ModifiedSuffixTrieConstruction(Text)
    compressed_tree = compress_tree(trie, Text)
    return compressed_tree

def count_leaves(node):
    if not isinstance(node, dict):
        return 0
    
    if '$END$' in node:
        return 1
    
    leaf_count = 0
    for key, child in node.items():
        if key != '$END$':
            leaf_count += count_leaves(child)
    
    return leaf_count

def find_longest_repeat(suffix_tree):
    longest_repeat = ""
    max_length = 0
    
    def dfs(node, current_string=""):
        nonlocal longest_repeat, max_length
        
        if not isinstance(node, dict):
            return
        
        leaf_count = count_leaves(node)
        
        if leaf_count >= 2 and len(current_string) > max_length:
            max_length = len(current_string)
            longest_repeat = current_string
        
        for key, child in node.items():
            if key != '$END$':
                dfs(child, current_string + key)
    
    dfs(suffix_tree)
    return longest_repeat

def find_all_repeats_brute_force(text):
    repeats = {}
    n = len(text)
    
    for i in range(n):
        for j in range(i+1, n+1):
            substring = text[i:j]
            if len(substring) > 0:
                positions = []
                for k in range(n - len(substring) + 1):
                    if text[k:k+len(substring)] == substring:
                        positions.append(k)
                if len(positions) >= 2:
                    repeats[substring] = positions
    
    longest = ""
    for substring in repeats:
        if len(substring) > len(longest):
            longest = substring
    
    return longest, repeats.get(longest, [])

def get_suffix_positions(node):
    positions = []
    
    def collect_positions(n):
        if not isinstance(n, dict):
            return
        
        if '$END$' in n:
            positions.append(n['$END$'])
        
        for key, child in n.items():
            if key != '$END$':
                collect_positions(child)
    
    collect_positions(node)
    return positions

def find_longest_repeat_with_positions(suffix_tree):
    longest_repeat = ""
    max_length = 0
    best_positions = []
    
    def dfs(node, current_string=""):
        nonlocal longest_repeat, max_length, best_positions
        
        if not isinstance(node, dict):
            return
        
        leaf_count = count_leaves(node)
        
        if leaf_count >= 2 and len(current_string) > max_length:
            max_length = len(current_string)
            longest_repeat = current_string
            best_positions = get_suffix_positions(node)
        
        for key, child in node.items():
            if key != '$END$':
                dfs(child, current_string + key)
    
    dfs(suffix_tree)
    return longest_repeat, best_positions

def find_all_repeats(suffix_tree):
    repeats = []
    
    def dfs(node, current_string=""):
        if not isinstance(node, dict):
            return
        
        leaf_count = count_leaves(node)
        
        if leaf_count >= 2 and current_string:
            repeats.append((current_string, leaf_count))
        
        for key, child in node.items():
            if key != '$END$':
                dfs(child, current_string + key)
    
    dfs(suffix_tree)
    return repeats

def print_tree_debug(node, depth=0, prefix="ROOT"):
    indent = "  " * depth
    if isinstance(node, dict):
        leaf_count = count_leaves(node)
        if '$END$' in node:
            print(f"{indent}{prefix} [LEAF: suffix {node['$END$']}]")
        else:
            print(f"{indent}{prefix} [Internal: {leaf_count} leaves]")
        
        for key, child in node.items():
            if key != '$END$':
                print_tree_debug(child, depth + 1, f"'{key}'")


with open("C:/Users/Matthew/Downloads/dataset_30222_5 (1).txt", 'r') as file:
    Text = file.read().strip()
#Text = "AGACAACCCTACCCTTTCACACAAACCTGATCGAGGGCTGTTCAATGTTACGGGGCTCGCTCTCGGAGAAAGCGACAATAGAAGCGTGGGCACGAATGCTCGACCCCGTGTGACTAATTCATGCACTTCACTGCAACCCATTGGCGGAACAGAAAGAAGTCGGCCCGGGATACCCGTCGGTACGGCGGGGACTCTAACTTCCTTATCCACAACCGAGTCCTACGTACCACAAACCATTTGCAGGGAACCCCCTCCATTAGTGGTATGTAGTGCATCTCGAGACCACTAAGCCGCATACCCTAGCGACGACCGGAAGAGTCGTCGAAAGGCATGAATCTTTCACCTTAAACCACCCGTTGAGACGTGGCGTGGGCACGAATGCTCGACCCCGTGTGACTAATTCATGCACTTCACTGCAACCCATTGGCGGAACAGAAAGAAGTCGGCCCGGGATACCCGTAGCGGGTACCCTACCTAGCCGGTTTATCATGCGGCCCAGATGGTTGTCTTTTGTGTTCGAAGTCTACCCGCAGCTCGACTACCCTCGAGCTAAATTGGGACGTCCACCCAGTTTTCAGATTGAATACACGGAACCTGGGTCTACCTACATCAGCCGGAGATCCTATCATTCGATTTTCAGGGTGCCTGAACAATCGTCCCGAATATAATTCATTGCTCTTATGCAGAGTAGCATCAGGGTTGACATGCGCTGGATTGTTGGTTGGCAGATTTAGGGTCGAATTGCGATGCAGGCATTGGGATCCCTTAACGATCTCTCGCAGTATCGACCAACTTTAGACCACAAAGGTATATTGGCACCTGAGGTCCAGCGAGTCAACACTCAAGAGTTTACCGTGCATCTTGCGTGGGCACGAATGCTCGACCCCGTGTGACTAATTCATGCACTTCACTGCAACCCATTGGCGGAACAGAAAGAAGTCGGCCCGGGATACCCGTGTCCCTATATCTGAGGGGCGAGTGCGGATCGCCGTCTTGTTGGATTACGCCGAGGGGCAAAACTGGAACAAACCATCAGCAAGCTAGGAACCTCAGTTATCCGGCCGATACACCTGATCCATGGCTACCCGGAGAAACCGCGGGACAGGTGGGAGCGCGATCAGCTCAAAACACCCGTCGATTTGGCTATGACGACAGGTATTCGGATCGCACGGCAGTGGTAACCGCTCGGCAACAATACCCCCGAAGAGGATATAGTTTTCCAGACTAATTAGGGCAGCTCCAGAGGAGAGGTCGTTTACCGGATTGGGGGTGGCAAAATACG"
#Might take up to 2 minutes
brute_longest, brute_positions = find_all_repeats_brute_force(Text)
if brute_positions:
    print(f"FINAL ANSWER: {brute_longest}")