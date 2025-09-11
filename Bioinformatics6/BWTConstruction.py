def CycleRotation(Text):
    CycleRot = [Text]
    for i in range(len(Text)-1):
        temp = Text[len(Text) - i -1:] + Text[:len(Text) - i -1]
        CycleRot.append(temp)
    return CycleRot

with open("C:/Users/Matthew/Downloads/dataset_30223_5.txt", 'r') as file:
    Text = file.read().strip()
'''
Sample Input:
GCGTGCCTGGTCA$

Sample Output:
ACTGGCT$TGCGGC
'''
res = CycleRotation(Text)
print("".join([i[-1] for i in sorted(res)]))