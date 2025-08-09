import copy

def EulerianPath(graph):
    g = copy.deepcopy(graph)
    outdeg = {u: len(v) for u, v in g.items()}
    indeg = {}
    for u in g:
        for v in g[u]:
            indeg[v] = indeg.get(v, 0) + 1
    #check if v already has an indegree count in the indeg dictionary.
    #If yes, return its current count.
    # If no, return 0 (the default).
    # Then + 1 → increment by 1 because you found another incoming edge to v.
    # If v was not in indeg, it gets initialized to 1.
    # If v was already counted before, it just increases the count.

    start = None
    end = None
    for node in set(list(outdeg.keys()) + list(indeg.keys())):
        out_d = outdeg.get(node, 0)
        in_d = indeg.get(node, 0)
        if out_d - in_d == 1:
            start = node
        elif in_d - out_d == 1:
            end = node
    if start is None:
        start = list(graph.keys())[0]

    stack = [start]
    path = []
    while stack:
        u = stack[-1]
        if u in g and g[u]:
            v = g[u].pop()
            stack.append(v)
        else:
            path.append(stack.pop())
    return path[::-1]

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
    return unbalanced

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

def StringSpelledByGappedPatterns(prefix, suffix, k, d):
    for i in range(k + d, len(prefix)):
        if prefix[i] != suffix[i - k - d]:
            return ""  # mismatch found
    return prefix[:k + d] + suffix

def ConstructStr(cycle, k, d):
    first_parts = []
    second_parts = []
    for node in cycle:
        a, b = node.split("|")
        first_parts.append(a)
        second_parts.append(b)

    prefix_string = first_parts[0]
    suffix_string = second_parts[0]
    for i in range(1, len(first_parts)):
        prefix_string += first_parts[i][-1]
        suffix_string += second_parts[i][-1]

    return StringSpelledByGappedPatterns(prefix_string, suffix_string, k, d)

with open('C:/Users/Matthew/Downloads/dataset_30188_16 (1).txt', 'r') as file:
    line = file.readlines()
k = 0
d = 0
k,d = line[0].strip().split(" ")
k = int(k)
d = int(d)
Text = line[1].strip().split(" ")
Map = {}
for i in Text:
    a, b = i.split("|")
    prefix = f"{a[:-1]}|{b[:-1]}"
    suffix = f"{a[1:]}|{b[1:]}"
    if prefix not in Map:
        Map[prefix] = [suffix]
    else:
        Map[prefix].append(suffix)
#print(Map)
tempMap = dict(Map)

unbalancedNode = unbalancedSearch(Map)
if not unbalancedNode:
    #Below code may have some errors
    visited, cycle = EulerianCycleBalance(tempMap)
else:
    cycle = EulerianPath(Map)
    res = ConstructStr(cycle,k,d)
    print(res)
    with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
        file.write(res)