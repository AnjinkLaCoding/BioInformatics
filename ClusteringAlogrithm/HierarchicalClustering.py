def hierarchical_clustering(distance_matrix):
    n = len(distance_matrix)
    # Initialize clusters - each point starts as its own cluster
    clusters = [[i] for i in range(n)]
    results = []
    while len(clusters) > 1:
        min_distance = float('inf')
        merge_i, merge_j = -1, -1
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distance = calculate_average_distance(clusters[i], clusters[j], distance_matrix)
                if distance < min_distance:
                    min_distance = distance
                    merge_i, merge_j = i, j
        new_cluster = clusters[merge_i] + clusters[merge_j]
        # Sort the new cluster for consistent output
        new_cluster.sort()
        # Add to results (convert from 0-indexed to 1-indexed)
        results.append([x + 1 for x in new_cluster])
        clusters.pop(max(merge_i, merge_j))
        clusters.pop(min(merge_i, merge_j))
        clusters.append(new_cluster)
    return results

def calculate_average_distance(cluster1, cluster2, distance_matrix):
    total_distance = 0
    count = 0
    for i in cluster1:
        for j in cluster2:
            total_distance += distance_matrix[i][j]
            count += 1
    return total_distance / count

'''
Sample Input:

7
0.00 0.74 0.85 0.54 0.83 0.92 0.89
0.74 0.00 1.59 1.35 1.20 1.48 1.55
0.85 1.59 0.00 0.63 1.13 0.69 0.73
0.54 1.35 0.63 0.00 0.66 0.43 0.88
0.83 1.20 1.13 0.66 0.00 0.72 0.55
0.92 1.48 0.69 0.43 0.72 0.00 0.80
0.89 1.55 0.73 0.88 0.55 0.80 0.00
'''
with open("C:/Users/Matthew/Downloads/dataset_30177_7.txt", 'r') as file:
    lines = file.read().strip().split('\n')
n = int(lines[0])
distance_matrix = []
for i in range(1, n + 1):
    row = list(map(float, lines[i].split()))
    distance_matrix.append(row)
results = hierarchical_clustering(distance_matrix)
for cluster in results:
    print(' '.join(map(str, cluster)))