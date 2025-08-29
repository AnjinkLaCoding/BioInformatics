AminoAcidImaginary = {4:"X", 5:"Z", 57:"G", 71:"A", 87:"S", 97:"P", 99:"V", 101:"T", 103:"C", 113:"L", 114:"N", 115:"D", 128:"Q", 129:"E", 131:"M", 137:"H", 147:"F", 156:"R", 163:"Y", 186:"W"}
AminoAcidImagRev = {"X":4, "Z":5, "G":57, "A":71, "S":87, "P":97, "V":99, "T":101, "C":103, "L":113, "N":114, "D":115, "Q":128, "E":129, "M":131, "H":137, "F":147, "R":156, "Y":163, "W":186, "I":113, "K":128}


def CountPeptide(peptide):
    res = 0 
    for i in peptide:
        if i in AminoAcidImagRev:
            res += AminoAcidImagRev[i]
    return res

def IdealSpectrum(Peptide):
    res = []
    for i in range(len(Peptide)):
        if i == len(Peptide)-1:
            res.append(CountPeptide(Peptide[0:]))
            return sorted(res)
        prefix = Peptide[0:i+1]
        res.append(CountPeptide(prefix))

def PeptideVector(Masses):
    n = max(Masses)
    res = []
    for i in range(n):
        if i+1 in Masses:
            res.append("1")
        else:
            res.append("0")
    return res

with open("C:/Users/Matthew/Downloads/dataset_30264_5.txt", "r") as f:
    Peptide = f.read()
#Input will in form of a string like below line
#Peptide = "XZZXX"
res = IdealSpectrum(Peptide)
print(res)
Vector = PeptideVector(res)
print(" ".join(Vector))
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for line in Vector:
        f.write(f"{line} ")