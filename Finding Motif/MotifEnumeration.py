def HammingDist(text, pattern):
    Coun = 0
    for i in range(len(pattern)):
        if text[i]!=pattern[i]:
            Coun+=1
    return Coun

#Function to search for the neighbour
def Neighbours(pattern, d):
    if d == 0:
        return pattern
    
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    
    neighbourhood = set()
    suffixNei = Neighbours(pattern[1:], d)
    for text in suffixNei:
        if HammingDist(text, pattern[1:]) < d:
            for nucleo in 'ACGT':
                neighbourhood.add(nucleo+text)
        else:
            neighbourhood.add(pattern[0]+text)
    Res = []
    for i in neighbourhood:
        Res += [i]
    return Res

#Function for motif enumeration
def MotifEnum(text, k, d):
    #Dict = MultipleStrNeighbour(text, k, d)
    patterns = set()
    for i in text:
        #print(i)
        for j in range(len(i)-k+1):
            for PatPrime in Neighbours(i[j:j+k], d):
                Coun = 0
                for Dna in text:
                    for m in range(len(Dna)-k+1):
                        if HammingDist(Dna[m:m+k], PatPrime) <= d:
                            Coun += 1
                            break
                if Coun == len(text):
                    patterns.add(PatPrime)
        #print(patterns)
    return [i for i in patterns]


Text = ['ATTGGCCGTCCAACAGAATGTACTA', 'TAGTTTTCCCTGTCCTTGTTCCGAC', 'CGTTACCGCCTTACCACCCGCTTCG', 'CCGTCGCTAGACGAGACGGTAATTC', 'CCGCCACCCACCTTCGATCGTATCG', 'GGGCCCCGTCCAATGGGATCTCCTG']
k = 5
d = 1
Res = MotifEnum(Text, k, d)
print(' '.join(Res))

#The answer is: CCCTC CCTTC CCGGC CCGAC CCGTC CCGCC
