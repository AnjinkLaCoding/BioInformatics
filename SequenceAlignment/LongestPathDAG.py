import math
from collections import defaultdict

def LongestPathDAG(start, end, edges):
    Graph = defaultdict(list)
    nodes = set()
    for u,v,w in edges:
        Graph[u].append((v,w))
        nodes.add(v)
        nodes.add(w)
    n = max(nodes) + 1
    dist = [-math.inf] * n
    parent = [None] * n
    dist[start] = 0
    for i in range(start,n):
        if dist[i] != -math.inf:
            for next, cost in Graph[i]:
                if dist[next] < dist[i] + cost:
                    dist[next] = dist[i] + cost
                    parent[next] = i
    path = []
    curr = end
    while curr != None:
        path.append(curr)
        curr = parent[curr]
    path = path[::-1]
    return dist[end], path

with open('C:/Users/Matthew/Downloads/dataset_30197_7.txt', 'r') as file:
    line = file.readlines()
start, end = map(int, line[0].split())
edges = [list(map(int, lines.split())) for lines in line[1:]]
#print(start, end)
#print(edges)
dist, res = LongestPathDAG(start, end, edges)
print(dist)
for i in range(len(res)):
    res[i] = str(res[i])
print(" ".join(res))
