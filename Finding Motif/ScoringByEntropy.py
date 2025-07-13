import math

def calculateLog2(Num):
    # using math.log2() to calculate log2
    if Num == 0:
        return 0
    else:
        res = math.log2(Num)
        return Num*res

Num = [[0.2, 0.1, 0.0, 0.7], [0.2, 0.2, 0.0, 0.6], [0.0, 0.0, 0.0, 1], [0.0, 0.0, 0.0, 1], [0.0, 0.0, 0.1, 0.9], [0.0, 0.0, 0.1, 0.9], [0.9, 0.0, 0.0, 0.1], [0.1, 0.4, 0.5, 0.0], [0.1, 0.1, 0.8, 0.0], [0.1, 0.2, 0.7, 0.0], [0.3, 0.4, 0.3, 0.0], [0.0, 0.6, 0.4, 0.0]]
res = 0
for i in range(len(Num)):
    sum = 0
    for j in range(4):
        sum += calculateLog2(Num[i][j])
    res += sum
print(res*-1)