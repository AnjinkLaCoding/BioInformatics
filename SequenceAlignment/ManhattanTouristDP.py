import numpy as np

def ManhattanTourist(n, m, Down, Right):
    S = np.empty((n+1, m+1))
    S[0][0] = 0
    for i in range(1,n+1):
        S[i][0] = S[i-1][0] + Down[i-1][0]
    for j in range(1,m+1):
        S[0][j] = S[0][j-1] + Right[0][j-1]
    for i in range(1,n+1):
        for j in range(1,m+1):
            S[i][j] = max(S[i-1][j] + Down[i-1][j], S[i][j-1] + Right[i][j-1])
    return S[n][m]

with open('C:/Users/Matthew/Downloads/dataset_ManhattanTouristDP.txt', 'r') as file:
    line = [lines.strip() for lines in file if lines.strip()]
n, m = map(int, line[0].split())
print(n,m)
SepIndex = line.index("-")
Down = np.array([list(map(int, lines.split())) for lines in line[1:SepIndex]])
Right = np.array([list(map(int, lines.split())) for lines in line[SepIndex + 1:]])
print(Down)
print(Right)
res = ManhattanTourist(n, m, Down, Right)

print(int(res))
