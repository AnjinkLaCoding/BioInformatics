from collections import defaultdict

def LimbLengthProblem(n, j, matrix):
    LimbLen = float('inf')
    for k in range(n):
        for i in range(n):
            if i != j and k != j and i != k:
                LimbLen = min(LimbLen, (matrix[i][j] + matrix[j][k] - matrix[i][k]) // 2)
    return LimbLen

def find_path(tree, start, end, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    visited.add(start)
    path.append(start)
    
    if start == end:
        return path[:]
    
    for neighbor in tree[start]:
        if neighbor not in visited:
            result = find_path(tree, neighbor, end, visited.copy(), path[:])
            if result:
                return result
    return None

def insert_node_on_path(tree, path, distance, next_node_id):
    total = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        edge_weight = tree[u][v]
        
        if total + edge_weight >= distance:
            # Insert new node on edge (u, v)
            new_node = next_node_id
            
            # Distance from u to new node
            dist_u_to_new = distance - total
            # Distance from new node to v
            dist_new_to_v = edge_weight - dist_u_to_new
            
            # Remove original edge
            del tree[u][v]
            del tree[v][u]
            
            # Create new node
            tree[new_node] = {}
            
            # Add edges: u -> new_node -> v
            tree[u][new_node] = dist_u_to_new
            tree[new_node][u] = dist_u_to_new
            tree[new_node][v] = dist_new_to_v
            tree[v][new_node] = dist_new_to_v
            
            return new_node
        
        total += edge_weight
    
    # If we reach here, the distance equals the total path length
    return path[-1]

def AdditivePhylogeny(D, next_node_id=None):
    n = len(D)
    
    if next_node_id is None:
        next_node_id = [n]  # Use list to make it mutable
    
    if n == 2:
        tree = {0: {1: D[0][1]}, 1: {0: D[0][1]}}
        return tree
    
    # Calculate limb length for last leaf
    limb_len = LimbLengthProblem(n, n-1, D)
    
    # Create a copy of D for modification
    D_modified = [row[:] for row in D]
    
    # Trim the limb
    for j in range(n-1):
        D_modified[j][n-1] -= limb_len
        D_modified[n-1][j] = D_modified[j][n-1]
    
    # Find i, k such that D[i,k] = D[i,n-1] + D[n-1,k]
    i = k = None
    for u in range(n-1):
        for v in range(n-1):
            if u != v and D_modified[u][v] == D_modified[u][n-1] + D_modified[n-1][v]:
                i, k = u, v
                break
        if i is not None:
            break
    
    x = D_modified[i][n-1]
    
    # Create reduced matrix
    D_reduced = []
    for row in range(n-1):
        D_reduced.append(D_modified[row][:n-1])
    
    # Recursive call
    Tree = AdditivePhylogeny(D_reduced, next_node_id)
    
    # Find path from i to k
    path = find_path(Tree, i, k)
    
    # Insert node at distance x from i
    v = insert_node_on_path(Tree, path, x, next_node_id[0])
    next_node_id[0] += 1
    
    # Add leaf n-1 back to tree
    leaf = n - 1
    Tree[leaf] = {v: limb_len}
    Tree[v][leaf] = limb_len
    
    return Tree

# Test with your matrix
D = [
    [0, 13, 21, 22],
    [13, 0, 12, 13],
    [21, 12, 0, 13],
    [22, 13, 13, 0]
]

with open('C:/Users/Matthew/Downloads/dataset_30286_6.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
n = int(lines[0])
D = []
for line in lines[1:]:
    row = list(map(int, line.split()))
    D.append(row)
Tree = AdditivePhylogeny(D)
for u in sorted(Tree.keys()):
    for v in sorted(Tree[u].keys()):
        print(f"{u}->{v}:{Tree[u][v]}")