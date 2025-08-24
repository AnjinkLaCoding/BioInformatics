def neighbor_joining(D, labels):
    n = len(D)

    if n == 2:
        return {
            labels[0]: {labels[1]: D[0][1]},
            labels[1]: {labels[0]: D[1][0]},
        }

    total = [sum(D[i]) for i in range(n)]

    # Build D* and pick (i,j) with i<j; tie-break by earliest in scan to match sample
    Dstar = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                Dstar[i][j] = (n - 2) * D[i][j] - total[i] - total[j]

    i, j = min(((i, j) for i in range(n-1) for j in range(i+1, n)),
               key=lambda x: Dstar[x[0]][x[1]])

    delta = (total[i] - total[j]) / (n - 2)
    limb_i = 0.5 * (D[i][j] + delta)
    limb_j = 0.5 * (D[i][j] - delta)

    m = max(labels) + 1  # next internal node id

    # Distances from new node m
    Dm = {}
    for k in range(n):
        if k != i and k != j:
            Dm[k] = 0.5 * (D[i][k] + D[j][k] - D[i][j])

    # Build reduced matrix
    keep = [k for k in range(n) if k not in (i, j)]
    idx = {k: t for t, k in enumerate(keep)}
    new_labels = [labels[k] for k in keep] + [m]
    size = len(keep) + 1
    new_D = [[0.0]*size for _ in range(size)]

    # Copy old distances
    for a in keep:
        for b in keep:
            new_D[idx[a]][idx[b]] = D[a][b]

    # Add m row/col
    for k in keep:
        dkm = Dm[k]
        new_D[idx[k]][size-1] = dkm
        new_D[size-1][idx[k]] = dkm

    T = neighbor_joining(new_D, new_labels)

    # Attach i and j to m
    T.setdefault(m, {})
    T.setdefault(labels[i], {})
    T.setdefault(labels[j], {})
    T[m][labels[i]] = limb_i
    T[labels[i]][m] = limb_i
    T[m][labels[j]] = limb_j
    T[labels[j]][m] = limb_j

    return T


def _clamp(x, eps=1e-9):
    return 0.0 if abs(x) < eps else x

def format_tree(T):
    edges = []
    for u, nbrs in T.items():
        for v, w in nbrs.items():
            edges.append((u, v, _clamp(w)))
    edges.sort(key=lambda e: (e[0], e[1]))
    return "\n".join(f"{u}->{v}:{w:.3f}" for u, v, w in edges)

with open('C:/Users/Matthew/Downloads/dataset_NeighbourJoining.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
n = int(lines[0])
D = []
for line in lines[1:]:
    row = list(map(int, line.split()))
    D.append(row)
labels = list(range(n))
tree = neighbor_joining(D, labels)
print(format_tree(tree))