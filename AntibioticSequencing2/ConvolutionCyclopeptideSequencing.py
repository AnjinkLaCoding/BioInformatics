from collections import Counter

def linear_spectrum(peptide):
    prefix = [0]
    for m in peptide:
        prefix.append(prefix[-1] + m)
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide)+1):
            spec.append(prefix[j] - prefix[i])
    return sorted(spec)

def cyclic_spectrum(peptide):
    prefix = [0]
    for m in peptide:
        prefix.append(prefix[-1] + m)
    pep_mass = prefix[-1]
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spec.append(prefix[j] - prefix[i])
            if i > 0 and j < len(peptide):
                spec.append(pep_mass - (prefix[j] - prefix[i]))
    return sorted(spec)

def score_spectrum(theo, exp):
    t = Counter(theo)
    e = Counter(exp)
    return sum(min(t[m], e[m]) for m in t)

def LinearScore(peptide, spectrum):
    return score_spectrum(linear_spectrum(peptide), spectrum)

def CyclicScore(peptide, spectrum):
    return score_spectrum(cyclic_spectrum(peptide), spectrum)

def Trim(leaderboard, spectrum, N):
    scored = [(pep, LinearScore(pep, spectrum)) for pep in leaderboard]
    scored.sort(key=lambda x: x[1], reverse=True)
    if len(scored) <= N:
        return [x[0] for x in scored]
    threshold = scored[N-1][1]
    return [pep for pep, s in scored if s >= threshold]

def LeaderboardCyclopeptideSequencing(spectrum, N, amino_acid_masses):
    leaderboard = [[]]
    leader_peptide = []
    parent_mass = max(spectrum)
    while leaderboard:
        new_leaderboard = []
        for peptide in leaderboard:
            for mass in amino_acid_masses:
                new_peptide = peptide + [mass]
                if sum(new_peptide) == parent_mass:
                    if CyclicScore(new_peptide, spectrum) > CyclicScore(leader_peptide, spectrum):
                        leader_peptide = new_peptide
                    new_leaderboard.append(new_peptide)
                elif sum(new_peptide) < parent_mass:
                    new_leaderboard.append(new_peptide)
        leaderboard = Trim(new_leaderboard, spectrum, N)
    return leader_peptide

def SpectralConvolutionProblem(spectrum):
    conv = []
    for i in range(len(spectrum)):
        for j in range(i):
            diff = spectrum[i] - spectrum[j]
            if 57 <= diff <= 200:
                conv.append(diff)
    return conv

def convolutionCyclopeptide(spectrum, M, N):
    spectrum.sort()
    conv = SpectralConvolutionProblem(spectrum)
    freq = Counter(conv)
    # Keep only valid amino acid masses
    filtered = [(mass, count) for mass, count in freq.items() if 57 <= mass <= 200]
    # Sort by frequency (desc), then mass (asc) to make ties deterministic
    sorted_filtered = sorted(filtered, key=lambda x: x[1], reverse=True)
    result_masses = []
    if sorted_filtered:
        threshold_count = sorted_filtered[min(M, len(sorted_filtered)) - 1][1]
        for mass, count in sorted_filtered:
            if count >= threshold_count:
                result_masses.append(mass)
    return LeaderboardCyclopeptideSequencing(spectrum, N, result_masses)

with open('C:/Users/Matthew/Downloads/dataset_ConvolutionCyclopeptide.txt', 'r') as file:
    line = file.readlines()
M = int(line[0].strip())
N = int(line[1].strip())
Spectrum = list(map(int, line[2].split()))
best_peptides = convolutionCyclopeptide(Spectrum, M, N)
res = []
for i in best_peptides:
    res.append(str(i))
print("-".join(res))