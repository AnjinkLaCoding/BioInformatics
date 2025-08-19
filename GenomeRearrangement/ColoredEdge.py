def ChromoToCycle(P):
    n  = len(P)*2
    nodes = [None]*n
    for i in range(len(P)):
        j = P[i]
        if j > 0:
            nodes[2*i] = 2*j-1
            nodes[2*i+1] = 2*j
        else:
            nodes[2*i] = -(2*j)
            nodes[2*i+1] = -(2*j)-1
    return nodes

def ColoredEdge(P):
    edges = []
    for i in P:
        nodes = ChromoToCycle(i)
        for j in range(len(i)):
            edges.append((nodes[2*j+1], nodes[(2*(j+1)) % (2*len(i))]))
    return edges

with open('C:/Users/Matthew/Downloads/dataset_30165_7 (1).txt', 'r') as file:
    line = file.read().strip()
genome = []
for chrom in line.split(')'):
    chrom = chrom.strip()
    if not chrom:
        continue
    # remove '(' and ')'
    chrom = chrom.strip('()')
    genes = list(map(int, chrom.split()))
    genome.append(genes)
res = ColoredEdge(genome)
print(res)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for i in res:
        f.write(f"{i}, ")