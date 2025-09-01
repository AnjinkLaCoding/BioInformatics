aa_table = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
            'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163,
            'X' : 4, 'Z' : 5}


def PeptideVector(peptide):
    prefixMasses = []
    for i in range(len(peptide)):
        prefixMasses.append(sum(peptide[:i + 1]))
    vector = [0] * prefixMasses[-1]
    for mass in prefixMasses:
        vector[mass - 1] = 1
    return vector


def PeptideIdentification(spectral_vector, proteome):
    max_score = -1e6
    mass_list = []
    for aa in proteome:
        mass_list.append(aa_table[aa])

    best_peptide = ''

    for i in range(len(mass_list)):
        k = 2
        while i + k < len(mass_list):
            peptide = mass_list[i:i + k]
            pep_vec = PeptideVector(peptide)
            if len(pep_vec) > len(spectral_vector):
                break
            if len(pep_vec) == len(spectral_vector):
                score = 0
                for idx in range(len(pep_vec)):
                    if pep_vec[idx] == 1:
                        score += spectral_vector[idx]
                if score > max_score:
                    max_score = score
                    best_peptide = proteome[i:i + k]
            k += 1
    return best_peptide

def Score(peptide, Spectrum):
    mass_list = []
    for aa in peptide:
        mass_list.append(aa_table[aa])
    pep_vec = PeptideVector(mass_list)
    if len(pep_vec) > len(Spectrum):
        return 0
    elif len(pep_vec) == len(Spectrum):
        score = 0
        for idx in range(len(pep_vec)):
            if pep_vec[idx] == 1:
                score += Spectrum[idx]
    return score

def PSMSearch(Vectors, proteome, threshold):
    PSMset = set()
    for Spectrum in Vectors:
        peptide = PeptideIdentification(Spectrum, proteome)
        if not peptide:
            continue
        if Score(peptide, Spectrum) >= threshold:
            PSMset.add(peptide)
    return PSMset

with open("C:/Users/Matthew/Downloads/dataset_30270_7 (1).txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]
#the input will be similar to this:
#-1 5 -4 5 3 -1 -4 5 -1 0 0 4 -1 0 1 4 4 4
#-4 2 -2 -4 4 -5 -1 4 -1 2 5 -3 -1 3 2 -3
#the spectral vector is all the above
#XXXZXZXXZXZXXXZXXZX - proteome
#5 - threshold
spectral_vectors = []
for line in lines[:-2]:  # everything except last 2 lines
    spectral_vectors.append(list(map(int, line.split())))
proteome = lines[-2]
threshold = int(lines[-1])
res = PSMSearch(spectral_vectors, proteome, threshold)
print(" ".join(map(str, res)))