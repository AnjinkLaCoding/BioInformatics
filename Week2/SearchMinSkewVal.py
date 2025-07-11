#Output the i size partof the genome if the value is the minimum

def MinSkew(text):
    Min=0
    Skew = 0
    Pos=[]
    for i in range(len(text)):
        if text[i] == 'C':
            Skew -= 1
        elif text[i] == 'G':
            Skew += 1
        
        if Skew < Min:
            Min = Skew
            Pos = []
            Pos += [str(i+1)]
        elif Skew == Min:
            Pos += [str(i+1)]
    return ' '.join(Pos)

#Change it with your file path
with open('C:/Users/Matthew/Downloads/dataset_30277.txt', 'r') as file:
    Text = file.read().strip()
Res = MinSkew(Text)
print(Res)

#The answer for this case is: first 69326 characters in the string inside Text
