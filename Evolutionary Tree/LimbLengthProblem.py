def LimbLengthProblem(n, j, matrix):
    LimbLen = 1000000
    for k in range(n):
        for i in range(n):
                if i != j and k != j:
                    LimbLen = min(LimbLen, int((matrix[i][j] + matrix[j][k] - matrix[i][k])/2))
    return LimbLen

with open('C:/Users/Matthew/Downloads/dataset_30285_11 (1).txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
n = int(lines[0])
j = int(lines[1])
matrix = []
for line in lines[2:]:
    row = list(map(int, line.split()))
    matrix.append(row)
res = LimbLengthProblem(n,j,matrix)
print(res)