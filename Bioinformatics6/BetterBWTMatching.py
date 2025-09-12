def PrecomputeCount(last):
    symbols = set([i for i in last])
    counts = {}
    for i in symbols:
        counts[i] = [0]
        count = 0
        for j in last:
            if j == i:
                count += 1
            counts[i].append(count)
    return counts

def BWTMatching(Seq, Pattern):
    last = [i for i in Seq]
    FirstOccur = {}
    for i, char in enumerate(sorted(last)):
        if char not in FirstOccur:
            FirstOccur[char] = i
    top = 0
    bottom = len(last) - 1
    PrecomCount = PrecomputeCount(last)
    while top <= bottom:
        if Pattern:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            if symbol in [last[i][0] for i in range(top, bottom + 1)]:
                top = FirstOccur[symbol] + PrecomCount[symbol][top]
                bottom = FirstOccur[symbol] + PrecomCount[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1

with open("C:/Users/B103040059/Downloads/dataset_30227_7 (3).txt", 'r') as file:
    Text = file.read().strip().split("\n")
'''
Sample Input:
GGCGCCGC$TAGTCACACACGCCGTA
ACC CCG CAG

Sample Output:
1 2 1
'''
Seq = Text[0]
Pattern = Text[1].split(" ")
#print(Seq)
res = []
for i in Pattern:
    res.append(str(BWTMatching(Seq, i)))
print(" ".join(res))
with open('C:/Users/B103040059/Downloads/Sol.txt', 'w') as f:
    f.write(" ".join(res))