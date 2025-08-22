import numpy as np

def UPGMA(Matrix, n):
    clusters = {i: [i] for i in range(n)}
    ages = {i: 0 for i in range(n)}
    next_cluster_id = n

    D = np.array(Matrix, dtype=float)
    active_clusters = set(range(n))
    tree = {}  # parent -> children

    while len(active_clusters) > 1:
        # Find closest pair
        min_dist = float("inf")
        ci, cj = -1, -1
        for i in active_clusters:
            for j in active_clusters:
                if i < j and D[i, j] < min_dist:
                    min_dist = D[i, j]
                    ci, cj = i, j

        # Merge clusters
        cnew = next_cluster_id
        next_cluster_id += 1
        tree[cnew] = [ci, cj]
        ages[cnew] = min_dist / 2

        # Update cluster contents
        clusters[cnew] = clusters[ci] + clusters[cj]

        # Update distances
        new_row = []
        for k in active_clusters:
            if k not in (ci, cj):
                dist = (len(clusters[ci]) * D[ci, k] +
                        len(clusters[cj]) * D[cj, k]) / (len(clusters[ci]) + len(clusters[cj]))
                new_row.append((k, dist))

        if cnew >= D.shape[0]:
            D = np.pad(D, ((0,1),(0,1)), 'constant', constant_values=0)

        for k, dist in new_row:
            D[cnew, k] = D[k, cnew] = dist

        active_clusters.remove(ci)
        active_clusters.remove(cj)
        active_clusters.add(cnew)
    root = list(active_clusters)[0]
    return tree, ages, root

def format_edges(tree, ages):
    edge_tuples = []
    for parent, children in tree.items():
        for child in children:
            length = ages[parent] - ages[child]
            edge_tuples.append((parent, child, length))
            edge_tuples.append((child, parent, length))  # symmetric

    # Sort by parent, then child
    edge_tuples.sort(key=lambda x: (x[0], x[1]))

    # Format with exactly 3 decimals
    return [f"{p}->{c}:{l:.3f}" for p, c, l in edge_tuples]


with open('C:/Users/Matthew/Downloads/dataset_UPGMA.txt', 'r') as f:
        n = int(f.readline().strip())
        matrix = [list(map(float, f.readline().split())) for _ in range(n)]
print(n)
print(matrix)
tree, ages, root = UPGMA(matrix, n)
edges = format_edges(tree, ages)
print("\n".join(edges))