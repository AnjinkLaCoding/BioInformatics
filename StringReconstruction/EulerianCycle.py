import random

#Step 1 is use to create a cycle
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

def Step2(start, visited, cycle, Graph):
    curr = start
    cycle, visited, Graph = Step1(start, Graph, curr, visited, cycle)
    return cycle, visited, Graph

def EulerianCycle(Graph):
    cycle = []
    start = random.choice(list(Graph.keys()))
    curr = start
    #print(curr)
    visited = []
    Tot_edge = sum(len(element) for element in Graph.values())
    #print(Tot_edge)
    cycle, visited, Graph = Step1(start, Graph, curr, visited, cycle)
    #print(visited)
    #print(cycle)
    #print(Graph)
    if len(visited) == Tot_edge:
        #print(visited)
        #print(cycle)
        #print("Done")
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
            cycle, visited, Graph = Step2(start, visited, cycle, Graph)
            #print("after step 2:")
            #print(visited)
            #print(cycle)
            #print(Graph)
            if len(cycle) == Tot_edge:
                cycle.append(visited[-1][1])
                break
        return visited, cycle

with open('C:/Users/Matthew/Downloads/dataset_30187_2.txt', 'r') as file:
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
#print(Map)
res, cycle = EulerianCycle(Map)
print(res)
print(cycle)
temp = []
#To write the answer where each element inside cycle is separated by whitespace
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    for i in cycle:
            file.write(f"{i} ")