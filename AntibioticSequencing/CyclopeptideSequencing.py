AminoMass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def LinearSpectrum(Peptides):
    PrefixMass = [0]
    for i in Peptides:
        PrefixMass.append(PrefixMass[-1] + i)
    LinearSpec = [0]
    for i in range(len(Peptides)):
        for j in range(i+1, len(Peptides)+1):
            LinearSpec.append(PrefixMass[j] - PrefixMass[i]) #Prefix have length len(PepStr) + 1
    return sorted(LinearSpec)

def CyclicSpectrum(Peptides):
    PrefixMass = [0]
    for i in Peptides:
        PrefixMass.append(PrefixMass[-1] + i)
    PeptideMass = PrefixMass[-1]
    CyclicSpec = [0]
    for i in range(len(Peptides)):
        for j in range(i+1, len(Peptides)+1):
            CyclicSpec.append(PrefixMass[j] - PrefixMass[i]) #Prefix have length len(PepStr) + 1
            if i > 0 and  j < len(Peptides):
                CyclicSpec.append(PeptideMass - (PrefixMass[j] - PrefixMass[i]))
    return sorted(CyclicSpec)

def expand(peptides):
    return [peptide + [mass] for peptide in peptides for mass in AminoMass]

def IsConsist(peptides, spectrum):
    peptide_counter = {}
    Peps = LinearSpectrum(peptides)
    for mass in Peps:
        peptide_counter[mass] = peptide_counter.get(mass, 0) + 1
    spectrum_counter = {}
    for mass in spectrum:
        spectrum_counter[mass] = spectrum_counter.get(mass, 0) + 1
    for i in peptide_counter:
        if peptide_counter[i] > spectrum_counter.get(i, 0):
            return False
    return True

def CyclopeptideSeq(spectrum):
    peptides = [[]]
    FinalPep = []
    ParentMass = max(spectrum)
    a = 0
    while peptides:
        peptides = expand(peptides)
        temp = []
        for i in peptides:
            if sum(i) == ParentMass:
                if CyclicSpectrum(i) == sorted(spectrum):
                    if i not in FinalPep:
                        FinalPep.append(i)
                peptides.remove(i)
            elif IsConsist(i, spectrum):
                temp.append(i)
        peptides = temp
    return FinalPep

with open("C:/Users/Matthew/Downloads/dataset_CyclopeptideSeq.txt", 'r') as file:
        line = file.readline().strip()
Spectrum = list(map(int, line.split()))
res = CyclopeptideSeq(Spectrum)
res.sort(reverse=True)
for peptide in res:
    print("-".join(map(str, peptide)))

