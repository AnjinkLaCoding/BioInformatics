def mlcs(v, w, u):
    n, m, l = len(v), len(w), len(u)
    # DP table
    dp = [[[0]*(l+1) for _ in range(m+1)] for __ in range(n+1)]

    # Fill DP
    for i in range(1, n+1):
        for j in range(1, m+1):
            for k in range(1, l+1):
                if v[i-1] == w[j-1] == u[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(
                        dp[i-1][j][k],
                        dp[i][j-1][k],
                        dp[i][j][k-1]
                    )

    # Backtrack
    a1, a2, a3 = [], [], []
    i, j, k = n, m, l
    while i > 0 or j > 0 or k > 0:
        if i > 0 and j > 0 and k > 0 and v[i-1] == w[j-1] == u[k-1] and dp[i][j][k] == dp[i-1][j-1][k-1] + 1:
            a1.append(v[i-1]); a2.append(w[j-1]); a3.append(u[k-1])
            i -= 1; j -= 1; k -= 1
        elif i > 0 and dp[i][j][k] == dp[i-1][j][k]:
            a1.append(v[i-1]); a2.append('-'); a3.append('-'); i -= 1
        elif j > 0 and dp[i][j][k] == dp[i][j-1][k]:
            a1.append('-'); a2.append(w[j-1]); a3.append('-'); j -= 1
        elif k > 0 and dp[i][j][k] == dp[i][j][k-1]:
            a1.append('-'); a2.append('-'); a3.append(u[k-1]); k -= 1
        else:
            # fallback (shouldn’t happen if dp built correctly)
            if i > 0: 
                a1.append(v[i-1]); a2.append('-'); a3.append('-'); i -= 1
            elif j > 0: 
                a1.append('-'); a2.append(w[j-1]); a3.append('-'); j -= 1
            elif k > 0: 
                a1.append('-'); a2.append('-'); a3.append(u[k-1]); k -= 1

    return dp[n][m][l], "".join(reversed(a1)), "".join(reversed(a2)), "".join(reversed(a3))

with open('C:/Users/Matthew/Downloads/dataset_30203_5.txt', 'r') as file:
    line = file.readlines()
v = line[0].strip()
w = line[1].strip()
u = line[2].strip()
score, a1, a2, a3 = mlcs(v, w, u)
print(score)
print(a1)
print(a2)
print(a3)