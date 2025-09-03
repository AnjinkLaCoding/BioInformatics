def squared_dist(p, q):
    return sum((pi - qi) ** 2 for pi, qi in zip(p, q))

def mean(points, m):
    return [sum(p[i] for p in points) / len(points) for i in range(m)]

def lloyd_algorithm(k, m, data):
    # Step 1: initialize centers as the first k points
    centers = [list(point) for point in data[:k]]
    
    while True:
        # Step 2: assign points to the nearest center
        clusters = [[] for _ in range(k)]
        for point in data:
            distances = [squared_dist(point, c) for c in centers]
            closest_center = distances.index(min(distances))
            clusters[closest_center].append(point)
        
        # Step 3: compute new centers
        new_centers = []
        for cluster in clusters:
            if cluster:  # avoid division by zero
                new_centers.append(mean(cluster, m))
            else:
                new_centers.append([0.0] * m)  # handle empty cluster
        
        # Step 4: check for convergence
        if all(all(abs(a - b) < 1e-6 for a, b in zip(c1, c2)) 
               for c1, c2 in zip(centers, new_centers)):
            break
        
        centers = new_centers
    
    return centers

with open("C:/Users/Matthew/Downloads/dataset_30171_3.txt", 'r') as file:
    lines = file.read().strip().split('\n')
k, m = map(int, lines[0].split())
data = []
for i in range(1, len(lines)):
    coordinates = list(map(float, lines[i].split()))
    data.append(coordinates)
#Input: Integers k and m followed by a set of points Data in m-dimensional space.
#Sample Input:
#2 2
#1.3 1.1
#1.3 0.2
#0.6 2.8
#3.0 3.2
#1.2 0.7
#1.4 1.6
#1.2 1.0
#1.2 1.1
#0.6 1.5
#1.8 2.6
#1.2 1.3
#1.2 1.0
#0.0 1.9

res = lloyd_algorithm(k, m, data)
for center in res:
    print(" ".join(f"{x:.3f}" for x in center))