#NGL this function is kinda feel like cheating
def ReconstructGenome(text):
    res = text[0]
    for i in text[1:]:
        res += i[-1]
    return res

#Replace the path below with the location of the dataset downloaded
with open('C:/Users/Matthew/Downloads/dataset_30182_3.txt', 'r') as file:
    line = file.readlines()
Text = [a.strip() for a in line]
Text = Text[0].split(" ")
res = ReconstructGenome(Text)
print(res)