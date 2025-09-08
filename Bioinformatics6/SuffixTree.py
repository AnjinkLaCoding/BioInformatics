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

def extract_edge_labels(tree):
    labels = []
    
    def dfs(node):
        if isinstance(node, dict):
            for key, child in node.items():
                if key != '$END$':
                    labels.append(key)
                    dfs(child)
    
    dfs(tree)
    return labels

def print_tree_debug(node, depth=0, prefix="ROOT"):
    indent = "  " * depth
    if isinstance(node, dict):
        if '$END$' in node:
            print(f"{indent}{prefix} [LEAF: suffix {node['$END$']}]")
        else:
            print(f"{indent}{prefix}")
        
        for key, child in node.items():
            if key != '$END$':
                print_tree_debug(child, depth + 1, f"'{key}'")

with open("C:/Users/Matthew/Downloads/dataset_30222_4 (1).txt", 'r') as file:
    Text = file.read().strip()
'''
Solve the Suffix Tree Construction Problem.
Input: A string Text.
Output: A space-separated list of the edge labels of SuffixTree(Text). You may return these strings in any order.

Sample Input:
ATAAATG$

Sample Output:
AAATG$ G$ T ATG$ TG$ A A AAATG$ G$ T G$ $
'''
suffix_tree = ModifiedSuffixTreeConstruction(Text)
labels = extract_edge_labels(suffix_tree)
print("Output (space-separated):")
print(' '.join(labels))
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(" ".join(labels))