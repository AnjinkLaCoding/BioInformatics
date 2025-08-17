def overlap_alignment(match_reward, mismatch_penalty, indel_penalty, v, w):
    n, m = len(v), len(w)

    S = [[0] * (m + 1) for _ in range(n + 1)]
    backtrack = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = S[i-1][j-1] + (match_reward if v[i-1] == w[j-1] else -mismatch_penalty)
            delete = S[i-1][j] - indel_penalty
            insert = S[i][j-1] - indel_penalty
            best = max(match, delete, insert)
            S[i][j] = best

            if best == match:
                backtrack[i][j] = "diag"
            elif best == delete:
                backtrack[i][j] = "up"
            else:
                backtrack[i][j] = "left"

    max_score = float("-inf")
    max_pos = (0, 0)
    for j in range(m + 1):
        if S[n][j] > max_score:
            max_score = S[n][j]
            max_pos = (n, j)
    for i in range(n + 1):
        if S[i][m] > max_score:
            max_score = S[i][m]
            max_pos = (i, m)
    i, j = max_pos
    aligned_v, aligned_w = [], []

    while i > 0 and j > 0:
        if backtrack[i][j] == "diag":
            aligned_v.append(v[i-1])
            aligned_w.append(w[j-1])
            i -= 1
            j -= 1
        elif backtrack[i][j] == "up":
            aligned_v.append(v[i-1])
            aligned_w.append("-")
            i -= 1
        elif backtrack[i][j] == "left":
            aligned_v.append("-")
            aligned_w.append(w[j-1])
            j -= 1
        else:
            break
    return max_score, "".join(reversed(aligned_v)), "".join(reversed(aligned_w))

with open('C:/Users/Matthew/Downloads/dataset_30200_7 (1).txt', 'r') as file:
    line = file.readlines()
match, missmatch, indels = map(int, line[0].split())
s = line[1].strip()
t = line[2].strip()
res, str1, str2 = overlap_alignment(match, missmatch, indels, s, t)
print(res)
print(str1)
print(str2)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(f"{str(res)}\n{str1}\n{str2}")