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

def LinearSpectrum(PepStr, AminoMass):
    PrefixMass = [0]
    for i in PepStr:
        PrefixMass.append(PrefixMass[-1] + AminoMass[i])
    LinearSpec = [0]
    for i in range(len(PepStr)):
        for j in range(i+1, len(PepStr)+1):
            LinearSpec.append(PrefixMass[j] - PrefixMass[i]) #Prefix have length len(PepStr) + 1
    return sorted(LinearSpec)

def score(Theore, experi):
    count = 0
    for i in Theore:
        if i in experi:
            count += 1
            experi.remove(i)
    return count
    
with open('C:/Users/Matthew/Downloads/dataset_LinearPepScore.txt', 'r') as file:
    line = file.readlines()
Text = line[0].strip()
Spectrum = list(map(int, line[1].split()))
theore = LinearSpectrum(Text, aminoAcidMass)
res = score(theore, Spectrum)
print(res)
