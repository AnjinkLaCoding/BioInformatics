import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def farthest_first_traversal(data, k):
    centers = []
    centers.append(data[0])
    for _ in range(k - 1):
        max_min_distance = -1
        farthest_point = None
        for point in data:
            if point in centers:
                continue
            min_distance = min(euclidean_distance(point, center) for center in centers)
            if min_distance > max_min_distance:
                max_min_distance = min_distance
                farthest_point = point
        if farthest_point is not None:
            centers.append(farthest_point)
    return centers

def format_output(centers):
    result = []
    for center in centers:
        formatted_coords = []
        for coord in center:
            if coord == float(coord):
                formatted_coords.append(str(float(coord)))
            else:
                formatted_coords.append(str(coord))
        result.append(' '.join(formatted_coords))
    return '\n'.join(result)

with open("C:/Users/Matthew/Downloads/dataset_30181_2.txt", 'r') as file:
    lines = file.read().strip().split('\n')
        
k, m = map(int, lines[0].split())
        
data = []
for i in range(1, len(lines)):
    coordinates = list(map(float, lines[i].split()))
    data.append(coordinates)
#The input will be similar to:
#3 2 - k & m
#0.0 0.0
#5.0 5.0
#0.0 5.0
#1.0 1.0
#2.0 2.0
#3.0 3.0
#1.0 2.0
centers = farthest_first_traversal(data, k)
output = format_output(centers)
print(output)