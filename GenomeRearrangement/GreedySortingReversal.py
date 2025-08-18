def SortingReversal(P, i):
    res = []
    for j in range(i, len(P)):
        if P[j] == i+1 or P[j] == -(i+1):
            index = j
    res = P[:i]
    for j in range(index, i-1, -1):
        res.append(P[j]*-1)
    res += P[index+1:]
    return res

def GreedySorting(P):
    Dist = []
    for i in range(len(P)):
        if P[i] != i+1 and P[i] != -(i+1):
            temp = []
            P = SortingReversal(P, i)
            temp = [f"{'+' if num > 0 else ''}{num}" for num in P]
            Dist.append(" ".join(temp))
        if P[i] == -(i+1):
            temp = []
            P[i] = P[i]*-1
            temp = [f"{'+' if num > 0 else ''}{num}" for num in P]
            Dist.append(" ".join(temp))
    return Dist

with open('C:/Users/Matthew/Downloads/dataset_30161_4 (3).txt', 'r') as file:
    line = file.readlines()
P = list(map(int, line[0].split()))
#P = [-3, +4, +1, +5, -2]
dist = GreedySorting(P)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for i in dist:
        f.write(f"{i}\n")