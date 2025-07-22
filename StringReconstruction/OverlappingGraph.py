def OverlappingGraph(text):
    Map = {}
    for i in text:
        Map[i] = []
    for i in range(len(text)):
        key = text.pop(i)
        suffix = key[1:]
        for j in range(len(text)):
            prefix = text[j][:-1]
            if suffix == prefix:
                Map[key] += [text[j]]
        text.insert(i, key)        
    return Map

with open("C:/Users/Matthew/Downloads/dataset_OverlappingGraph.txt", "r") as file:
    Text = file.read().split()
res = OverlappingGraph(Text)
#Write the answer into a text file and just directly copy paste it, change the solution location
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    for node, edges in res.items():
            for edge in edges:
                file.write(f"{node} : {edge}\n")

