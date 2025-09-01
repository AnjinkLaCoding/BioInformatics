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

with open("C:/Users/Matthew/Downloads/dataset_30270_2.txt", "r") as f:
    lines = f.read().strip().splitlines()
#Input example:
#Spectrum = 0 0 0 4 -2 -3 -1 -7 6 5 3 2 1 9 3 -8 0 3 1 2 1 8
#proteom = XZZXZXXXZXZZXZXXZ
Spectrum = list(map(int, lines[0].split()))
Proteome = lines[1].strip()
res = PeptideIdentification(Spectrum, Proteome)
print(res)