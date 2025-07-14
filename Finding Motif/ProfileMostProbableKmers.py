def ProfileMostProbable(text, k, MotifMatrix):
    Kmer = ''
    PrevProb = 0
    for i in range(len(text)- k + 1):
        Prob = 1
        Coun = 0
        for j in text[i:i+k]:
            if j == 'A':
                Prob = Prob*MotifMatrix[0][Coun]
            elif j == 'C':
                Prob = Prob*MotifMatrix[1][Coun]
            elif j == 'G':
                Prob = Prob*MotifMatrix[2][Coun]
            else:
                Prob = Prob*MotifMatrix[3][Coun]
            Coun += 1
        if Prob > PrevProb:
            PrevProb = Prob
            Kmer = text[i:i+k]
    return Kmer

#We need to use below code to get the dna
with open('C:/Users/Matthew/Downloads/dataset_ProfileMost.txt', 'r') as file:
    line = file.readlines()

Text = line[0].strip()
k = int(line[1].strip())  # everything after first line
MatElse = line[2:]
Matrix = []
#Strip the string
for a in MatElse:
    temp = a.strip()
    Matrix.append(temp.split(" "))
#Cinvert it from string into floating number
for a in range(len(Matrix)):
    for b in range(len(Matrix[a])):
        Matrix[a][b] = float(Matrix[a][b])
res = ProfileMostProbable(Text, k, Matrix)
print(res)

#The answer is: AGCAACAAGAATGGC