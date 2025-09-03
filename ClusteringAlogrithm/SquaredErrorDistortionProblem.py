def SquaredDist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def CalcDistortion(data, centers):
    n = len(data)
    k = len(centers)
    res = 0
    distances = []
    #n = num of data point
    #k = num of centers
    for i in range(n):
        DataDist = []
        for j in range(k):
            d = SquaredDist(data[i], centers[j])
            DataDist.append(d)
        distances.append(min(DataDist))
    res = sum(distances)/n
    return res



with open("C:/Users/Matthew/Downloads/dataset_30170_3.txt", "r") as f:
        lines = f.read().strip().splitlines()
        k, m = map(int, lines[0].split())
        sep_index = next(i for i, line in enumerate(lines) if set(line) == {'-'})
        centers = [tuple(map(float, line.split())) for line in lines[1:sep_index]]
        data = [tuple(map(float, line.split())) for line in lines[sep_index + 1:]]
#The input is similar to below:
#Input: Integers k and m, followed by a set of centers Centers and a set of points Data.
#2 2
#2.31 4.55
#5.96 9.08
#--------
#3.42 6.03
#6.23 8.25
#4.76 1.64
#4.47 4.33
#3.95 7.61
#8.93 2.97
#9.74 4.03
#1.73 1.28
#9.72 5.01
#7.27 3.77
print(f"{CalcDistortion(data, centers):.3f}")
