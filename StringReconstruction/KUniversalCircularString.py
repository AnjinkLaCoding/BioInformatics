import random

def generateBinary(n):
    return [format(i, f'0{n}b') for i in range(2**n)]

def GenerateGraph(text, k):
    Map = {}
    for i in text:
        prefix = i[:-1]
        suffix = i[1:]
        if prefix not in Map:
            Map[prefix] = [suffix]
        else:
            Map[prefix].append(suffix)
    return Map

def Step1s(start, Graph, curr, visited, cycle, unbalanced, Tot_edge):
    flag = ''
    while True:
        if curr not in Graph:
            flag = unbalanced[curr]
            cycle.append(curr)
            break
        for i in Graph[curr]:
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
    return cycle, visited, Graph, flag

def EulerianPath(Graph, start, unbalanced):
    cycle = []
    curr = start
    visited = []
    flag = ''
    Tot_edge = sum(len(element) for element in Graph.values())
    cycle, visited, Graph, flag = Step1s(start, Graph, curr, visited, cycle, unbalanced, Tot_edge)
    if flag == 'Outdeg':
        start = ""
        for i in cycle:
            if i in unbalanced and unbalanced[i] == 'Outdeg':
                continue
            if Graph[i]:
                start = i
                break
        if not Graph:
            return visited, cycle
        if start == "":
            return visited, cycle
        curr = start
        index = len(cycle) - 1
        cycle, visited, Graph, flag = Step1(start, Graph, curr, visited, cycle, unbalanced, Tot_edge)
        indexFirst = cycle.index(cycle[index+1])
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

def ConstructStr(res):
    stringres = res[0]
    k = len(res[0]) + 1
    res.pop(0)
    for i in range(len(res)):
        temp = res[i][-1]
        stringres += temp
    end = 2**k
    #print(end)
    #print(stringres)
    return stringres[:end]

def Step1(start, Graph, curr, visited, cycle):
    while True:
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
        if curr == start and not Graph[curr]:
            break   
    return cycle, visited, Graph

def EulerianCycleBalance(Graph):
    cycle = []
    start = [i for i in Graph.keys()][0]
    #print(start)
    curr = start
    visited = []
    Tot_edge = sum(len(element) for element in Graph.values())
    cycle, visited, Graph = Step1(start, Graph, curr, visited, cycle)
    if len(visited) == Tot_edge:
        cycle.append(visited[-1][1])
        return visited, cycle
    else:
        #if there are unvisited edges inside the graph
        while True:
            start = 0
            for i in cycle:
                if Graph[i]:
                    start = i
                    break
            index = cycle.index(start)
            cycle = cycle[index:] + cycle[:index]
            visited = visited[index:] + visited[:index]
            curr = start
            cycle, visited, Graph = Step1(start, Graph, curr, visited, cycle)
            if len(cycle) == Tot_edge:
                cycle.append(visited[-1][1])
                break
        return visited, cycle

k = 8
res = generateBinary(k)
Map = GenerateGraph(res, k)
#print(res)
#print(Map)
unbalancedNode, newmap = unbalancedSearch(Map)
start = 0
#print(unbalancedNode)
if not unbalancedNode:
    visited, cycle = EulerianCycleBalance(Map)
    #print(visited)
    #print(cycle)
    results = ConstructStr(cycle)
    #print(results)
else:
    for i in unbalancedNode:
        if unbalancedNode[i] == 'Indeg':
            start = i
    visited, cycle = EulerianPath(Map, start, unbalancedNode)
    results = ConstructStr(cycle)
    #print(results)
#visited, cycle = EulerianPath(Map, start, unbalancedNode)
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    file.write(results)

# the answer is 1111111011111100111110101111100011110110111101001111001011110000111011101100111010101110100011100110111001001110001011100000110110101101100011010100110100101101000011001100101011001000110001001100001011000000101010100010100100101000001001000010001000000001
#For K = 8