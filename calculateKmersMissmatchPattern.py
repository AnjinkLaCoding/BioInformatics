
#To calcualte the hamming distance between two string
def HammingDist(text, pattern):
    Coun = 0
    for i in range(len(pattern)):
        if text[i]!=pattern[i]:
            Coun+=1
    return Coun

#Calculate the number of possible k-mers with only d missmatches from the pattern
def SearchMiss(text, pattern, d):
    Pos = []
    for i in range(len(text)-len(pattern)+1):
        if HammingDist(text[i:i+len(pattern)], pattern) <= d:
            Pos += [str(i)]
    return len(Pos)

Text = 'AACAAGCTGATAAACATTTAAAGAG'
pattern = 'AAAAA'
d = 2
res = SearchMiss(Text, pattern, d)
print(res)

#the answer is : 11