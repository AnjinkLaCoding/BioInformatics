import random

def Step1(start, Graph, curr, visited, cycle, unbalanced, Tot_edge):
    flag = ''
    while True:
        if curr not in Graph:
            flag = unbalanced[curr]
            #print(flag)
            cycle.append(curr)
            break
        for i in Graph[curr]:
            #print(i)
            if [curr,i] in visited:
                continue
            else:
                temp = [curr,i]
                visited.append(temp)
                cycle.append(curr)
                Graph[curr].remove(i) #Delete the visited node from the Graph
                curr = i
                break
        if curr == start or len(cycle) == Tot_edge or not Graph[curr]:
            if curr in unbalanced and unbalanced[curr] == 'Outdeg':
                flag = unbalanced[curr]
            cycle.append(curr)
            break
    #print(f"Setelah step 1: {cycle} {flag}")
    return cycle, visited, Graph, flag

def EulerianPath(Graph, start, unbalanced):
    cycle = []
    curr = start
    visited = []
    flag = ''
    Tot_edge = sum(len(element) for element in Graph.values())
    cycle, visited, Graph, flag = Step1(start, Graph, curr, visited, cycle, unbalanced, Tot_edge)
    #print(cycle)
    #print(visited)
    if flag == 'Outdeg':
        #print(Graph)
        for i in cycle:
            if Graph[i]:
                start = i
                break
        if not Graph:
            return visited, cycle
        #print(start)
        curr = start
        #print(Graph)
        index = len(cycle) - 1
        #print(f"index dari unbalanced node: {index}")
        cycle, visited, Graph, flag = Step1(start, Graph, curr, visited, cycle, unbalanced, Tot_edge)
        #print(cycle)
        indexFirst = cycle.index(cycle[index+1])
        #print(indexFirst)
        cycle = cycle[:indexFirst] + cycle[index+1:] + cycle[indexFirst:index+1]
    return visited, cycle

def unbalancedSearch(Map):
    unbalanced = {}
    #map has the value [Indegree, Outdegree] for each node i
    Newmap = {}
    indeg = 0
    outdeg = 0
    keys = [i for i in Map.keys()]
    for i in keys:
        if i not in Newmap:
            Newmap[i] = [0,0]
        val = [j for j in Map[i]]
        for k in val:
            if k not in Newmap:
                Newmap[k] = [0,0]
            Newmap[i][1] += 1
            Newmap[k][0] += 1
    for key, value in Newmap.items():
        if value[0] != value[1]:
            if value[0] < value[1]:
                unbalanced[key] = "Indeg"
            else:
                unbalanced[key] = "Outdeg"
    return unbalanced, Newmap

with open('C:/Users/Matthew/Downloads/dataset_30187_6 (1).txt', 'r') as file:
    line = file.readlines()
Map = {}
res = []
for val in line:
    res = val.strip()
    i = res.index(':')
    key = int(res[:i])
    val = res[i+2:].split()
    val = [int(i) for i in val]
    Map[key] = val
print(Map)
unbalancedNode, newmap = unbalancedSearch(Map)
#print(unbalancedNode)
#print(newmap) #To see which node is unbalanced
start = 0
for i in unbalancedNode:
    if unbalancedNode[i] == 'Indeg':
        start = i
print(unbalancedNode)
visited, cycle = EulerianPath(Map, start, unbalancedNode)
print(visited)
print(cycle)
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    for i in cycle:
        file.write(f"{i} ")


