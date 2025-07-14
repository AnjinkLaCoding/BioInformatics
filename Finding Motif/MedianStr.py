def HammingDist(text, pattern):
    Coun = 0
    for i in range(len(pattern)):
        if text[i]!=pattern[i]:
            Coun+=1
    return Coun

def MedianStr(text, pattern):
    distance = 0
    for i in range(len(text)):
        hammingDist = len(text[i])
        for j in range(len(text[i])-len(pattern)+1):
            if hammingDist > HammingDist(text[i][j:j+len(pattern)], pattern):
                hammingDist = HammingDist(text[i][j:j+len(pattern)], pattern)
        distance += hammingDist
    return distance

Text = []
pattern  = ''
with open('C:/Users/Matthew/Downloads/dataset_30312_1.txt', 'r') as file:
    line = file.readlines()

pattern = line[0].strip()
text_lines = line[1:]  # everything after first line
Text = [line.strip() for line in text_lines]
Text = Text[0].split(" ")
res = MedianStr(Text, pattern)
print(res)