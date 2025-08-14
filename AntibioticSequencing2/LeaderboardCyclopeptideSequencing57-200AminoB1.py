from collections import Counter

# The unique integer masses of the 18 amino acids
AminoMass = [i for i in range(57, 201)]

def expand(peptides):
    """Expand each peptide by adding one of the 18 masses."""
    return [pep + [m] for pep in peptides for m in AminoMass]

def linear_spectrum(peptide):
    """Generate the linear spectrum of a peptide."""
    prefix = [0]
    for m in peptide:
        prefix.append(prefix[-1] + m)
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spec.append(prefix[j] - prefix[i])
    return sorted(spec)

def cyclic_spectrum(peptide):
    """Generate the cyclic spectrum of a peptide."""
    prefix = [0]
    for m in peptide:
        prefix.append(prefix[-1] + m)
    pep_mass = prefix[-1]
    spec = [0]
    for i in range(len(peptide)):
        for j in range(i+1, len(peptide)+1):
            spec.append(prefix[j] - prefix[i])
            if i > 0 and j < len(peptide):
                spec.append(pep_mass - (prefix[j] - prefix[i]))
    return sorted(spec)

def score_spectrum(theo, exp):
    """Score a theoretical spectrum against an experimental one (multiset score)."""
    t = Counter(theo)
    e = Counter(exp)
    return sum(min(t[m], e[m]) for m in t.keys())

def LinearScore(peptide, spectrum):
    return score_spectrum(linear_spectrum(peptide), spectrum)

def CyclicScore(peptide, spectrum):
    return score_spectrum(cyclic_spectrum(peptide), spectrum)

def Trim(leaderboard, spectrum, N, ParentMass):
    """Keep top N peptides by linear score, but never drop full-mass peptides."""
    scored = [(LinearScore(pep, spectrum), pep) for pep in leaderboard]
    scored.sort(key=lambda x: x[0], reverse=True)
    if len(scored) <= N:
        return [pep for _, pep in scored]
    cutoff = scored[N-1][0]
    trimmed = []
    for s, pep in scored:
        if s >= cutoff or sum(pep) == ParentMass:
            trimmed.append(pep)
    return trimmed

def LeaderboardCyclopeptideSequencing(Spectrum, N):
    """Leaderboard algorithm returning ALL peptides with the maximum cyclic score."""
    LeaderBoard = [[]]
    ParentMass = max(Spectrum)
    best_score = -1
    best_peptides = []
    while LeaderBoard:
        LeaderBoard = expand(LeaderBoard)
        NewLeaderboard = []
        for pep in LeaderBoard:
            mass = sum(pep)
            if mass == ParentMass:
                cscore = CyclicScore(pep, Spectrum)
                if cscore > best_score:
                    best_score = cscore
                    best_peptides = [pep]
                elif cscore == best_score:
                    best_peptides.append(pep)
                NewLeaderboard.append(pep)  # keep full-mass peptides
            elif mass < ParentMass:
                NewLeaderboard.append(pep)
            # if mass > ParentMass, drop it automatically
        LeaderBoard = Trim(NewLeaderboard, Spectrum, N, ParentMass)
    return best_score, best_peptides

with open('C:/Users/Matthew/Downloads/dataset_30245_2.txt', 'r') as file:
    line = file.readlines()
N =int(line[0].strip())
Spectrum = list(map(int, line[1].split()))
#print(N)
#print(Spectrum)
#N = 10
#Spectrum = [0, 71, 113, 129, 147, 200, 218, 260, 313, 331, 347, 389, 460]
best_score, best_peptides = LeaderboardCyclopeptideSequencing(Spectrum, N)

# Format as requested: peptides in integer format, separated by space
def peptide_to_str(pep):
    return '-'.join(map(str, pep))

answer_str = ' '.join(peptide_to_str(p) for p in best_peptides) #Change to separated by space in this code
print(answer_str)

with open('Spectrum25_best_linear_peptides.txt', 'w') as f:
    f.write(answer_str)