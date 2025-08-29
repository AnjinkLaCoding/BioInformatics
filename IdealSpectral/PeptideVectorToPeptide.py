AminoAcidImaginary = {4:"X", 5:"Z", 57:"G", 71:"A", 87:"S", 97:"P", 99:"V", 101:"T", 103:"C", 113:"L", 114:"N", 115:"D", 128:"Q", 129:"E", 131:"M", 137:"H", 147:"F", 156:"R", 163:"Y", 186:"W"}
AminoAcidImagRev = {"X":4, "Z":5, "G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "L":113, "N":114, "D":115, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186, "I":113, "K":128}

def Getmasses(vector):
    res = []
    for i in range(len(vector)):
        if vector[i] == 1:
            res.append(i+1)
    return res

def ToPeptide(masses):
    res = ""
    prev = 0
    for i in masses:
        if i-prev in AminoAcidImaginary:
            res+=AminoAcidImaginary[i-prev]
            prev = i
    return res

with open("C:/Users/Matthew/Downloads/dataset_30264_6.txt", "r") as f:
    Vector = list(map(int, f.read().split()))
#The input is a peptide vector [0, 0, 1, 0,.....]
res = Getmasses(Vector)
#print(res)
Peptide = ToPeptide(res)
print(Peptide)