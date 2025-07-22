def DebruijnGraph(text, k):
    Map = {}
    for i in range(len(text) - k + 1):
        prefix = text[i:i+k-1]
        suffix = text[i+1:i+k]
        if prefix in Map:
             Map[prefix].append(suffix)
        else:
             Map[prefix] = [suffix]   
    return Map

Text = ''
k = 0
with open('C:/Users/Matthew/Downloads/dataset_DeBruijnGraph.txt', 'r') as file:
    line = file.readlines()
k = line[0].strip()
k = int(k)
Text = line[1].strip()
res = DebruijnGraph(Text, k)
res = dict(sorted(res.items()))
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    for node, edges in res.items():
            file.write(f"{node} : {' '.join(edges)}\n")

