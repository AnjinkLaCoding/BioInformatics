def DeBruijnFromKmer(text, k):
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

def Step1(start, Graph, curr, visited, cycle, unbalanced, Tot_edge):
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
    cycle, visited, Graph, flag = Step1(start, Graph, curr, visited, cycle, unbalanced, Tot_edge)
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
    k = len(cycle[0])
    res.pop(0)
    for i in range(len(res)):
        temp = res[i][-1]
        stringres += temp
    return stringres
            
with open('C:/Users/Matthew/Downloads/StringReconstructionDataset.txt', 'r') as file:
    line = file.readlines()
k = line[0].strip()
Text = line[1].strip().split(' ')
#Generate DeBruijn Graph from Kmers
res = DeBruijnFromKmer(Text, k)
res = dict(sorted(res.items()))
unbalancedNode, newmap = unbalancedSearch(res)
start = 0
for i in unbalancedNode:
    if unbalancedNode[i] == 'Indeg':
        start = i
#Generate the eulerian path
visited, cycle = EulerianPath(res, start, unbalancedNode)
#Generate the genome
res = ConstructStr(cycle)
print(res)