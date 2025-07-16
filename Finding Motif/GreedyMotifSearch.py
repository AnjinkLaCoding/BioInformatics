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
                p[nuc][i] = Coun/t
    return p

def GreedyMotif(text, k, t):
    best_motif = [item[:k] for item in text]
    for i in range(len(text[0])- k + 1):
        motifs = []
        motifs = [text[0][i:i+k]]
        #Below Function will only use the first kmer of t-1 string from t string, the probableKmer from last string will not be used to update the profile
        for j in range(1,t):
                profile = ProfileMaking(motifs, k)
                ProbableKmer = ProfileMostProbable(text[j], k, profile)
                motifs.append(ProbableKmer)
        if score(motifs) < score(best_motif):
            best_motif = motifs
    return ' '.join(best_motif)
    

Text = []
k  = 0
t = 0
#We need to use below code to get the dna
with open('C:/Users/Matthew/Downloads/dataset_GreedyMotifSearch.txt', 'r') as file:
    line = file.readlines()

k,t = line[0].strip().split(" ")
k = int(k)
t = int(t)
text_lines = line[1:]  # everything after first line
Text = [line.strip() for line in text_lines]
Text = Text[0].split(" ")
res = GreedyMotif(Text, k, t)
print(res)

#the asnwer is : GTTCTCGCGCAG GCTTGAGAAGAA ACGCCGAGCACC ACGCAGAACTCC ATGCTCAGGCCG ATGCCGAGCACC ACGCTCAGAACG ATGCGGACCACC ATGCTGAGCACC ACGCCGAACGCC ATGCCGACCACC ACGCTGAACTCC AGTTTGGCCGAG ATGCAGAACTCC GTGTCGAAGCAC AGGCGGACCACC ATGCTGAGCGCC ATGCCGACCGCC ATGCTGAGCACC ACGCAGAGCACC ATGCCGAGCTCC AGGCGGAACACC TGCTTATCTAGT ACGCGGAGCGCC ACGCAGACCGCC

