def RevCom(Text):
    res = ""
    for i in Text:
        if i == 'A':
            res+='T'
        elif i == 'C':
            res+='G'
        elif i == 'G':
            res+='C'
        else:
            res+='A'
    return res

def ChangeT(Text):
    res = ""
    for i in range(len(Text)):
        if Text[i] == 'T':
            res += 'U'
        else:
            res+=Text[i]
    return res

def RevertBackDna(Text):
    res = ""
    for i in range(len(Text)):
        if Text[i] == 'U':
            res += 'T'
        else:
            res+=Text[i]
    return res

def PeptideEncoding(Text, Pep, ProteinMap):
    res = []
    k = len(Pep) * 3
    PepLen = 3
    for i in range(len(Text) - k + 1):
        dna = Text[i:i+k]
        rev = dna[::-1]
        rev = RevCom(rev)
        dna = ChangeT(dna)
        rev = ChangeT(rev)
        #print(f"{dna} {rev}")
        revtemp = ""
        dnatemp = ""
        for j in range(0, len(dna), PepLen):
            revtemp += ProteinMap[rev[j:j+PepLen]]
            dnatemp += ProteinMap[dna[j:j+PepLen]]
        #print(f"{dnatemp} {revtemp}")
        if dnatemp == Pep or revtemp == Pep:
            dna = RevertBackDna(dna)
            res.append(dna)
    return res


with open('C:/Users/Matthew/Downloads/RNA_codon_table_1.txt', 'r') as file:
    line = file.readlines()
ProteinMap = {}
for i in line:
    c = i.strip().split(" ")
    if len(c) == 2:
        ProteinMap[c[0]] = c[1]
    else:
        ProteinMap[c[0]] = ""
with open('C:/Users/Matthew/Downloads/dataset_PeptideEncodingProblem.txt', 'r') as file:
    line = file.readlines()
Text = line[0].strip()
Pep = line[1].strip()
#print(Text)
#print(Pep)
#Text = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
#Pep = "MA"
res = PeptideEncoding(Text, Pep, ProteinMap)
print(res)
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    for i in res:
        if i != "":
            file.write(f"\n{i}")