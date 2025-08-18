def CycleToChromosome(nodes):
    P = [None] * (int(len(nodes)/2))
    for i in range(int(len(nodes)/2)):
        if nodes[2*i] < nodes[2*i+1]:
            P[i] = int(nodes[2*i+1] / 2)
        else:
            P[i] = -(int(nodes[2*i] / 2))
    return P

#nodes = [1, 2, 4, 3, 6, 5, 7, 8]
with open('C:/Users/Matthew/Downloads/dataset_30165_5.txt', 'r') as file:
    line = file.read().strip()
nodes = list(map(int, line.strip("()").split()))
res = CycleToChromosome(nodes)
temp = [f"{'+' if num > 0 else ''}{num}" for num in res]
res = "(" + " ".join(temp) + ")"
print(res)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(res)