def SpectralConvolutionProblem(Spectrum):
    res = []
    for i in range(1,len(Spectrum)):
        for j in range(i):
            if Spectrum[i] - Spectrum[j] > 0:
                res.append(Spectrum[i] - Spectrum[j])
    return res

with open('C:/Users/Matthew/Downloads/dataset_30246_4.txt', 'r') as file:
    line = file.readlines()
Spectrum = list(map(int, line[0].split()))
print(Spectrum)
res = SpectralConvolutionProblem(Spectrum)
#res.sort(reverse=True)
temp = []
for i in res:
    temp.append(str(i))
print(' '.join(temp))