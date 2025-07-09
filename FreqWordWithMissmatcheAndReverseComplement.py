#Calculate hamming Distance
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
    return neighbourhood

#Function to return the reverse complement of a string
def RevCom(text):
    Comp = ''
    for i in text:
        if i == 'A':
            Comp+='T'
        elif i == 'C':
            Comp+='G'
        elif i == 'G':
            Comp+='C'
        else:
            Comp+='A'
    return Comp[::-1]

#below function is use to search for the frequent word, and search for the neighbour of the frequent word with missmatches up to d and its reverse complement
def FreqWordMissmatchRevComp(text, k, d):
    pattern = ''
    map = {}
    Neighbourhood = set()
    Res = []
    for i in range (len(text) - k + 1):
        pattern = text[i:i+k]
        Neighbourhood = Neighbours(pattern, d)
        for j in Neighbourhood:
            if j in map:
                map[j] += 1
            else:
                map[j] = 1
            if RevCom(j) in map:
                map[RevCom(j)] += 1
            else:
                map[RevCom(j)] = 1
    maxKmers = max(map.values())
    for key, freq in map.items():
        if map[key] == maxKmers:
            Res += [key]
    return ' '.join(Res)

Text = 'GTCGCGCGCCCGACGTACCCTGCCCTGCACACACACTGCCCGTTGCCGACGTCGCGCGGTACACACGTCCCCACACCCGTTGCCGGTGTCGCCTGCTGCACTGCACACTGCTGCGTCGTGCTGCTGCCCCGCGTGCACGTCGGTGTCCGTTGCACCGCGTGCGTCGGTGTGTACGTCGTGCTGCACTGCCCGTACTGCCGGTACGTCGCCACCCTGCACGTGTACTGCTGCGTTGCGTACCCAC'
k = 5
d = 3
res = FreqWordMissmatchRevComp(Text, k, d)
print(res)

#The answer is : GGGCC GGCCC