def NumBreakpoint(P):
    n = len(P)
    Permu = [0] + P + [n+1]
    BP = 0
    for i in range(len(Permu) - 1):
        if Permu[i+1] - Permu[i] != 1:
            BP += 1
    return BP

with open('C:/Users/Matthew/Downloads/dataset_30162_6.txt', 'r') as file:
    line = file.readlines()
P = list(map(int, line[0].split()))
res = NumBreakpoint(P)
print(res)