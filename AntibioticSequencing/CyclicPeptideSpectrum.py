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
    PeptideMass = PrefixMass[-1]
    CyclicSpec = [0]
    for i in range(len(PepStr)):
        for j in range(i+1, len(PepStr)+1):
            CyclicSpec.append(PrefixMass[j] - PrefixMass[i]) #Prefix have length len(PepStr) + 1
            if i > 0 and  j < len(PepStr):
                CyclicSpec.append(PeptideMass - (PrefixMass[j] - PrefixMass[i]))
    return sorted(CyclicSpec)

Text = "IPPWRVIYHWEIWT"
res = LinearSpectrum(Text, aminoAcidMass)
print(*LinearSpectrum(Text, aminoAcidMass), sep=' ')