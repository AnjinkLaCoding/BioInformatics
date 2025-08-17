def global_alignment(match, mismatch, indel, s, t):
    m, n = len(s), len(t)
    dp = [[-10**9] * (n+1) for _ in range(m+1)]
    dp[0][0] = 0
    #Initializing indels value on index 0
    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] - indel
    for j in range(1, n+1):
        dp[0][j] = dp[0][j-1] - indel
    # CalculatingRecurrence
    for i in range(1, m+1):
        for j in range(1, n+1):
            score_diag = dp[i-1][j-1] + (match if s[i-1] == t[j-1] else -mismatch)
            score_up = dp[i-1][j] - indel
            score_left = dp[i][j-1] - indel
            dp[i][j] = max(score_diag, score_up, score_left)

    aligned_s = []
    aligned_t = []
    i, j = m, n
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            diag_score = dp[i-1][j-1] + (match if s[i-1] == t[j-1] else -mismatch)
            if dp[i][j] == diag_score:
                aligned_s.append(s[i-1])
                aligned_t.append(t[j-1])
                i -= 1; j -= 1
                continue
        if i > 0:
            up_score = dp[i-1][j] - indel
            if dp[i][j] == up_score:
                aligned_s.append(s[i-1])
                aligned_t.append('-')
                i -= 1
                continue
        # otherwise must be left
        aligned_s.append('-')
        aligned_t.append(t[j-1])
        j -= 1

    aligned_s.reverse()
    aligned_t.reverse()
    return dp[m][n], ''.join(aligned_s), ''.join(aligned_t)

with open('C:/Users/Matthew/Downloads/dataset_30199_3 (1).txt', 'r') as file:
    line = file.readlines()
match, penalty, indels = map(int, line[0].split())
s = line[1].strip()
t = line[2].strip()
score, str1, str2 = global_alignment(match, penalty, indels, s,t)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(f"{str(score)}\n{str1}\n{str2}")