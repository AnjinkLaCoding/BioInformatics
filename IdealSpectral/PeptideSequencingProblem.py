import math

AminoAcidImagRev = {"X":4, "Z":5, "G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "L":113, "N":114, "D":115, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186, "I":113, "K":128}
AminoAcid = {57:"G", 71:"A", 87:"S", 97:"P", 99:"V", 101:"T", 103:"C", 113:"L", 114:"N", 115:"D", 128:"Q", 129:"E", 131:"M", 137:"H", 147:"F", 156:"R", 163:"Y", 186:"W"}

def PeptideSeq(Spectrum):
    n = len(Spectrum)
    dist = [-math.inf] * n
    path = [""] * n
    dist[0] = 0
    for i in range(1,n):
        for mass, pep in AminoAcid.items():
            #print(f"The i and mass now is {i} and {pep}")
            a = i - mass
            #print(a)
            if a >= 0:
                temp = dist[a] + Spectrum[i]
                if temp > dist[i]:
                    dist[i] = temp
                    path[i] = path[a] + pep
    return path[-1]


with open("C:/Users/Matthew/Downloads/dataset_30264_13 (2).txt", "r") as f:
    Spectrum = list(map(int, f.read().split()))
#Below is the example of the input
#Spectrum = [0, 0, 0, 4, -2, -3, -1, -7, 6, 5, 3, 2, 1, 9, 3, -8, 0, 3, 1, 2, 1, 8]
NewS = [0] + Spectrum
res = PeptideSeq(NewS)
print(res)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(res)