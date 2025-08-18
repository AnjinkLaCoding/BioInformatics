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

with open('C:/Users/Matthew/Downloads/dataset_30165_4 (1).txt', 'r') as file:
    line = file.read().strip()
P = list(map(int, line.strip("()").split()))
print(P)
res = ChromoToCycle(P)
temp = "(" + " ".join(map(str, res)) + ")"
print(temp)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(temp)