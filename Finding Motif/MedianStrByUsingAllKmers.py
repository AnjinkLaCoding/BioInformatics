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
    return list(neighbourhood)

def MedianStr(text, k):
    distance = len(text[0])
    median = ''
    for i in range(len(text)):
        for j in range(len(text[i]) - k + 1):
            patterns = Neighbours(text[i][j:j+k], k)
            for m in patterns:
                if distance > HammingDist(text[i][j:j+k], m):
                    distance = HammingDist(text[i][j:j+k], m)
                    median = m
    return median

Text = []
pattern  = ''
#We need to use below code to get the dna
with open('C:/Users/Matthew/Downloads/dataset_30304_9.txt', 'r') as file:
    line = file.readlines()

k = int(line[0].strip())
text_lines = line[1:]  # everything after first line
Text = [line.strip() for line in text_lines]
res = MedianStr(Text, k)
print(res)

#The dna sequences is: 
# TGTTGAGACCTATGTAGCGGTAAAAACTTTATCTGGAAGCCT, AAACTACGCACATAGGCAGGCTGCATTTCCCACTCATGCAGC, TGAAGCACTCTCTCACGTCACTAACCGGACAGAGACTTCAGG
#TAAGAACGTATGTAAGCCTGTAGCAAAATCTGATACGAGGTT, GTAGTATGTAGCGCCTGAACTATGATAATTGAAAGGCATACG, CGGATGGCAGTATGTGTCTTGCCAGTGCTCTGAAGCTGGGGG
#TGCAGCACCTCCTCCTGAATGGCTGATCCAGACCAAGGATTC, CACTATCCGGTGATCTCCTACAGGGCTTGGTGTAGCAGACCT, CGTACCCTCTCCGCTGGTTGGAGCTTGTTATCCTACAGTGGT
#TTTGCCTACTTCTGGAGCTGCAGGTCTTACGCCGATACCTCA

#The answer is TGTTGA