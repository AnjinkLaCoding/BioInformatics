def DeBruijnFromKmer(text):
    k = len(text[0]) - 1
    prefix = ''
    suffix = ''
    Map = {}
    for i in text:
        prefix = i[:-1]
        suffix = i[1:]
        if prefix in Map:
            Map[prefix].append(suffix)
        else:
            Map[prefix] = [suffix]
    return Map

with open('C:/Users/Matthew/Downloads/dataset_30184_8.txt', 'r') as file:
    line = file.readlines()
Text = line[0].strip().split(' ')
res = DeBruijnFromKmer(Text)
res = dict(sorted(res.items()))
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    for node, edges in res.items():
            file.write(f"{node} : {' '.join(edges)}\n")