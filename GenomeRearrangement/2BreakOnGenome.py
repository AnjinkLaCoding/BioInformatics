def BreakonGenomeGraph(Graph, i1, i2, i3, i4):
    for i in Graph:
        if i == [i1, i2] or i == [i2, i1] or i == [i3, i4] or i == [i4, i3]:
            Graph.remove(i)
    Graph.append([i1, i3])
    Graph.append([i2, i4])
    return Graph

with open('C:/Users/Matthew/Downloads/dataset_30166_2 (1).txt', 'r') as file:
    lines = file.readlines()
line1 = lines[0].strip()
Graph = [list(map(int, pair.strip('() ').split(','))) for pair in line1.split('),')]
line2 = lines[1].strip()  # "1, 6, 3, 8"
values = list(map(int, line2.split(',')))
i1 = values[0];i2 = values[1];i3 = values[2];i4 = values[3]
#Graph = [[2, 4], [3, 8], [7, 5], [6, 1]]
#i1 = 1;i2 = 6;i3 = 3;i4 = 8
res = BreakonGenomeGraph(Graph, i1, i2, i3, i4)
formatted = ', '.join(f'({a}, {b})' for a, b in res)
print(formatted)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(formatted)

