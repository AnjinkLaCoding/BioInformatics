from collections import Counter
import copy

AminoMass = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

def expand(peptides):
    return [peptide + [mass] for peptide in peptides for mass in AminoMass]

def Trim(leaderboard, spectrum, N):
    scored = [(score(pep, spectrum), pep) for pep in leaderboard]
    scored.sort(reverse=True, key=lambda x: x[0])
    if len(scored) <= N:
        return [pep for _, pep in scored]
    cutoff = scored[N - 1][0]
    return [pep for s, pep in scored if s >= cutoff]

def score(peptide, spectrum):
    theo_spectrum = CyclicSpectrum(peptide)
    exp = copy.deepcopy(spectrum)
    count = 0
    for m in theo_spectrum:
        if m in exp:
            count += 1
            exp.remove(m)
    return count

def CyclicSpectrum(peptide):
    prefix_mass = [0]
    for m in peptide:
        prefix_mass.append(prefix_mass[-1] + m)
    peptide_mass = prefix_mass[-1]
    cyclic_spec = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            cyclic_spec.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < len(peptide):
                cyclic_spec.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(cyclic_spec)

def is_consistent(peptide, spectrum):
    spectrum_counter = Counter(spectrum)
    prefix_mass = [0]
    for m in peptide:
        prefix_mass.append(prefix_mass[-1] + m)
    lin_spec = []
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            lin_spec.append(prefix_mass[j] - prefix_mass[i])
    lin_counter = Counter(lin_spec)
    for mass, count in lin_counter.items():
        if count > spectrum_counter.get(mass, 0):
            return False
    return True

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    LeaderBoard = [[]]
    LeaderPeptide = []
    ParentMass = max(Spectrum)
    while LeaderBoard:
        LeaderBoard = expand(LeaderBoard)
        NewLeaderboard = []
        for pep in LeaderBoard:
            mass = sum(pep)
            if mass == ParentMass:
                if score(pep, Spectrum) > score(LeaderPeptide, Spectrum):
                    LeaderPeptide = pep
                NewLeaderboard.append(pep)
            elif mass < ParentMass:
                #We need to check if the peptide LinearSpectrum is consistent with the experimental spectrum
                if is_consistent(pep, Spectrum):
                    NewLeaderboard.append(pep)
        LeaderBoard = Trim(NewLeaderboard, Spectrum, N)
    return LeaderPeptide

with open('C:/Users/Matthew/Downloads/dataset_LeaderboardCyclopeptideSeq.txt', 'r') as file:
    line = file.readlines()
N =int(line[0].strip())
Spectrum = list(map(int, line[1].split()))
#print(N)
#print(Spectrum)
#N = 10
#Spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
res = LeaderboardCyclopeptideSequencing(Spectrum, N)
temp = []
for i in res:
    temp.append(str(i))
print('-'.join(temp))

