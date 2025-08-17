def middle_edge(v, w, match_reward, mismatch_penalty, indel_penalty):
    n, m = len(v), len(w)
    mid = m // 2

    match = match_reward
    mismatch = -mismatch_penalty
    indel = -indel_penalty

    # Forward DP
    prev = [i * indel for i in range(n + 1)]
    for j in range(1, mid + 1):
        curr = [j * indel]
        for i in range(1, n + 1):
            score = match if v[i - 1] == w[j - 1] else mismatch
            curr.append(max(
                prev[i] + indel,
                curr[-1] + indel,
                prev[i - 1] + score
            ))
        prev = curr
    score_left = prev

    # Backward DP
    v_rev, w_rev = v[::-1], w[::-1]
    mid_rev = m - mid
    prev = [i * indel for i in range(n + 1)]
    for j in range(1, mid_rev + 1):
        curr = [j * indel]
        for i in range(1, n + 1):
            score = match if v_rev[i - 1] == w_rev[j - 1] else mismatch
            curr.append(max(
                prev[i] + indel,
                curr[-1] + indel,
                prev[i - 1] + score
            ))
        prev = curr
    score_right = prev[::-1]

    # Find split row
    split_row, max_score = 0, -10**9
    for i in range(n + 1):
        s = score_left[i] + score_right[i]
        if s > max_score:
            max_score, split_row = s, i

    # Determine edge direction with priority: right > down > diagonal
    best_dir = None
    best_val = -10**9

    if mid < m:  # right
        right = score_left[split_row] + indel + score_right[split_row]
        if right > best_val:
            best_val, best_dir = right, (split_row, mid + 1)

    if split_row < n:  # down
        down = score_left[split_row] + indel + score_right[split_row + 1]
        if down > best_val:
            best_val, best_dir = down, (split_row + 1, mid)

    if split_row < n and mid < m:  # diagonal
        diag = score_left[split_row] + (match if v[split_row] == w[mid] else mismatch) + score_right[split_row + 1]
        if diag > best_val:
            best_val, best_dir = diag, (split_row + 1, mid + 1)

    # Convert both nodes to 1-based coordinates
    start = (split_row, mid)
    end = best_dir
    return (start[0], start[1]), (end[0], end[1])

with open('C:/Users/Matthew/Downloads/dataset_30202_12 (1).txt', 'r') as file:
    line = file.readlines()
match, missmatch, indels = map(int, line[0].split())
t = line[1].strip()
s = line[2].strip()
edge = middle_edge(s, t, match, missmatch, indels)
print(edge[0][0], edge[0][1])
print(edge[1][0], edge[1][1])