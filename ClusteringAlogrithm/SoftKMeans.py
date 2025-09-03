import math
import numpy as np
'''
Sample Input:
2 2
2.7
1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9
'''

def read_data():
    f = open("C:/Users/Matthew/Downloads/dataset_30291_9.txt", 'r')
    raw = f.read().strip().split()
    f.close()
    k, m = int(raw[0]), int(raw[1])
    stiffness = float(raw[2])
    raw_data = raw[3:]
    
    data = []
    for i in range(len(raw_data) // m):
        point = [float(d) for d in raw_data[i * m:(i + 1) * m]]
        data.append(point)
    
    return k, stiffness, np.array(data)

def euclidean_distance(p1, p2):
    return math.sqrt(np.sum((p1 - p2)**2))

def soft_k_means(data, k, stiffness, max_iterations=100):
    n, m = data.shape
    centers = data[:k, :].copy()
    
    for _ in range(max_iterations):
        # E-step: Compute hidden matrix (responsibilities)
        hidden_matrix = np.zeros((k, n))
        for i in range(k):
            for j in range(n):
                hidden_matrix[i, j] = math.exp(-stiffness * euclidean_distance(data[j, :], centers[i, :]))
        
        # Normalize the rows of the hidden matrix
        for j in range(n):
            row_sum = np.sum(hidden_matrix[:, j])
            if row_sum > 0:
                hidden_matrix[:, j] /= row_sum
        
        # M-step: Update centers
        new_centers = np.zeros_like(centers)
        for i in range(k):
            numerator = np.dot(hidden_matrix[i, :], data)
            denominator = np.sum(hidden_matrix[i, :])
            if denominator > 0:
                new_centers[i, :] = numerator / denominator
        
        centers = new_centers
        
    return centers

def format_output(centers):
    output_lines = []
    for center in centers:
        formatted_coords = [f"{coord:.3f}" for coord in center]
        output_lines.append(" ".join(formatted_coords))
    return "\n".join(output_lines)

def main():
    k, stiffness, data = read_data()
    centers = soft_k_means(data, k, stiffness)
    output = format_output(centers)
    print(output)
    
if __name__ == '__main__':
    main()