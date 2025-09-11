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


with open("C:/Users/Matthew/Downloads/dataset_30233_6 (4).txt", 'r') as f:
    content = f.read()
'''
Sample Input:
0:
1:
2: 0 1
3:
4:
5: 2 3
6:
7: 4 5 6
-
0 red
1 red
3 blue
4 blue
6 red

Sample Output:
0 red
1 red
2 red
3 blue
4 blue
5 purple
6 red
7 purple
'''
sections = content.strip().split('-')
tree_lines = sections[0].strip().splitlines()
prop_lines = sections[1].strip().splitlines()

tree = {}
for line in tree_lines:
    if ':' not in line:
        continue
    key_str, children_str = line.split(':')
    key = int(key_str.strip())
    if children_str.strip():  # Has children
        children = list(map(int, children_str.strip().split()))
        tree[key] = children

Colors = {}
for line in prop_lines:
    if line.strip():
        node_str, value = line.strip().split()
        node = int(node_str)
        Colors[node] = value
print(tree)
print(Colors)
res = TreeColoring(tree, Colors)
res = dict(sorted(res.items()))
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for keys,vals in res.items():
        f.write(f"{keys} {vals}\n")