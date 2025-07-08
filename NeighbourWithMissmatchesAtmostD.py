def HammingDist(text, pattern):
    Coun = 0
    for i in range(len(pattern)):
        if text[i]!=pattern[i]:
            Coun+=1
    return Coun

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

Text = 'TCGCTTAC'
d = 2
res = Neighbours(Text, d)
print(' '.join(res))

# the answer for this question is just print above code 