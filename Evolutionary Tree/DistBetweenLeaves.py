import numpy as np
from collections import defaultdict

def DistanceBetweenLeaves(n, Graph):
    NumKeys = len(Graph)
    DistMatrix = [[1000000] * NumKeys for _ in range(NumKeys)]
    for i in range(NumKeys):
        DistMatrix[i][i] = 0
    for u in Graph:
        for v, w in Graph[u]:
            DistMatrix[u][v] = w
    #print(DistMatrix)
    #print(NumKeys)
    for k in range(NumKeys):
        for i in range(NumKeys):
            for j in range(NumKeys):
                if DistMatrix[i][k] != 1000000 and DistMatrix[k][j] != 1000000:
                    DistMatrix[i][j] = min(DistMatrix[i][j], DistMatrix[i][k] + DistMatrix[k][j])
    return DistMatrix

with open('C:/Users/Matthew/Downloads/dataset_DistBetweenLeaves.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
n = int(lines[0])
res = defaultdict(list)
for line in lines[1:]:
    left, right = line.split("->")
    src = int(left)
    dst, val = map(int, right.split(":"))
    res[src].append([dst, val])

# convert back to normal dict if you like
Graph = dict(res)
res = DistanceBetweenLeaves(n, Graph)
for i in range(n):

    print(" ".join(map(str, res[i][:n])))
