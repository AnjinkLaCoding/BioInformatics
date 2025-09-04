from collections import defaultdict

def generate_output(tree_dict):
    result = []
    node_counter = 1  # Start from 1 since root is 0
    stack = []
    initial_items = list(tree_dict.items())
    #Stack is LIFO
    for char, child in reversed(initial_items):
        if char != 'end':
            stack.append((child, 0, char))
    while stack:
        current_node, parent_id, char = stack.pop()
        current_id = node_counter
        node_counter += 1
        result.append(f"{parent_id} {current_id} {char}")
        # Add children to stack in reverse order (for LIFO processing)
        items = list(current_node.items())
        for child_char, child_node in reversed(items):
            if child_char != 'end':
                stack.append((child_node, current_id, child_char))
    return result

def TrieConstruct(str):
    Tree = defaultdict(lambda: defaultdict(list))
    for i in str:
        node = Tree
        for j in range(len(i)):
            if i[j] not in node:
                node[i[j]] = {}
            node = node[i[j]]
        node['end'] = True
    res = generate_output(Tree)
    return res


with open("C:/Users/Matthew/Downloads/dataset_30220_4.txt", 'r') as file:
    lines = file.read().strip().split(' ')
'''
Sample Input:
ATAGA ATC GAT

Sample Output:
0 1 A
1 2 T
2 3 A
3 4 G
4 5 A
2 6 C
0 7 G
7 8 A
8 9 T
'''
str = []
for i in lines:
    str.append(i)
res = TrieConstruct(str)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write("\n".join(res))