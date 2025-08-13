aminoAcidMass = {
    'G': 57,
    'A': 71,
    'S': 87,
    'P': 97,
    'V': 99,
    'T': 101,
    'C': 103,
    'I': 113, 
    'L': 113,
    'N': 114,
    'D': 115,
    'K': 128,
    'Q': 128,
    'E': 129, 
    'M': 131, 
    'H': 137, 
    'F': 147, 
    'R': 156, 
    'Y': 163,
    'W': 186
}

def CyclicSpectrum(PepStr, AminoMass):
    PrefixMass = [0]
    for i in PepStr:
        PrefixMass.append(PrefixMass[-1] + AminoMass[i])
    PeptideMass = PrefixMass[-1]
    CyclicSpec = [0]
    for i in range(len(PepStr)):
        for j in range(i+1, len(PepStr)+1):
            CyclicSpec.append(PrefixMass[j] - PrefixMass[i]) #Prefix have length len(PepStr) + 1
            if i > 0 and  j < len(PepStr):
                CyclicSpec.append(PeptideMass - (PrefixMass[j] - PrefixMass[i]))
    return sorted(CyclicSpec)

with open('C:/Users/Matthew/Downloads/dataset_30244_3 (1).txt', 'r') as file:
    line = file.readlines()
Text = line[0].strip()
Spectrum = list(map(int, line[1].split()))
#print(Text)
#print(Spectrum)
res = CyclicSpectrum(Text, aminoAcidMass)
print(*CyclicSpectrum(Text, aminoAcidMass), sep=' ')
count = 0
for i in res:
    if i in Spectrum:
        count += 1
        Spectrum.remove(i)
print(count)