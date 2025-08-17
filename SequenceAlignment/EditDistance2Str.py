def EditDistance(s, t):
    m = len(s)
    n = len(t)
    S = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m+1):
        S[i][0] = i
    for j in range(1, n+1):
        S[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if s[i-1] == t[j-1] else 1
            S[i][j] = min(S[i-1][j] + 1, S[i][j-1] + 1, S[i-1][j-1] + cost)
    return S[m][n]

with open('C:/Users/Matthew/Downloads/dataset_30200_3 (2).txt', 'r') as file:
    line = file.readlines()
s = line[0].strip()
t = line[1].strip()
res = EditDistance(s,t)
print(res)