import random

def ProfileMostProbable(text, k, MotifMatrix):
    Kmer = ''
    PrevProb = 0
    for i in range(len(text)- k + 1):
        Prob = 1
        Coun = 0
        for j in text[i:i+k]:
            if j == 'A':
                Prob = Prob*MotifMatrix['A'][Coun]
            elif j == 'C':
                Prob = Prob*MotifMatrix['C'][Coun]
            elif j == 'G':
                Prob = Prob*MotifMatrix['G'][Coun]
            else:
                Prob = Prob*MotifMatrix['T'][Coun]
            Coun += 1
        if Prob > PrevProb:
            PrevProb = Prob
            Kmer = text[i:i+k]
    if PrevProb == 0:
        Kmer = text[0:k]
    return Kmer

def score(motifs):
    #Return the sum of the lowercase letter per column
    k = len(motifs[0])
    t = len(motifs)
    res = 0
    for i in range(k):
        maxVal = 0
        col = [motif[i] for motif in motifs]
        maxVal = max(col.count(nucle) for nucle in 'ACGT')
        res += t-maxVal
    return res


def ProfileMaking(motifs, k):
    p = {nucleo:[0]*k for nucleo in 'ACGT'}
    t = len(motifs)
    for i in range(k):
        temp = []
        for j in range(t):
            temp.append(motifs[j][i])
            for nuc in 'ACGT':
                Coun = temp.count(nuc)
                p[nuc][i] = Coun+1
    sum = 0
    for i in range(k):
        for j in 'ACGT':
            sum += p[j][i]
        for j in 'ACGT':
            p[j][i] = p[j][i]/sum
    return p

def MotifFromProfile(text, k, profile, t):
    motifs = []
    for i in range(t):
        temp = ProfileMostProbable(text[i], k, profile)
        motifs.append(temp)
    return motifs


def RandomizedMotifSearch(text, k, t):
    motifs = []
    for dna_string in text:
        start_index = random.randint(0, len(dna_string) - k)
        motifs.append(dna_string[start_index:start_index + k])
    best_motif = motifs
    while True:
        profile = ProfileMaking(motifs, k)
        motifs = MotifFromProfile(text, k, profile, t)
        if score(motifs) < score(best_motif):
            best_motif = motifs
        else:
            return best_motif

Text = []
k  = 0
t = 0
res = []
with open('C:/Users/Matthew/Downloads/dataset_RandomizedMotifSearch.txt', 'r') as file:
    line = file.readlines()

k,t = line[0].strip().split(" ")
k = int(k)
t = int(t)
text_lines = line[1:]  # everything after first line
Text = [line.strip() for line in text_lines]
Text = Text[0].split(" ")
#Iterate for 1000 times
for i in range(1000):
    temp = RandomizedMotifSearch(Text, k, t)
    res.append(temp)
Result = min(res, key=score)
print(' '.join(Result))

#The answer : GCCAGCAAGGTTCTC GACATCACGGTCCTT CCCTGTACGGTCCTC GCTAGTACGGTCCTT TACTGTACGGTCCCC GACTGCCGGGTCCTT GACTGTCTCGTCCTT GAGAATACGGTCCTT GACTGAGAGGTCCTT GACTGTACGGTCAAC GACTGTACGGTGGAT GACTGTACGTCTCTT GACTGTCTTGTCCTT CTATGTACGGTCCTT GACCCCACGGTCCTT GACTAAGCGGTCCTT GACTCATCGGTCCTT GACTGTACGGCGATT GACTGTACCCACCTT GACTGTAAATTCCTT