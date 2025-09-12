from collections import defaultdict
# Yields each character with the occurrence number
def index_seq(seq):
    d = defaultdict(int)
    for c in seq:
        yield c, d[c]
        #Returns the character and its current occurrence count (0-indexed)
        #Second time seeing 'A': yields ('A', 1), then increments count to 2
        d[c] += 1
    return d

def BWTMatching(Seq, Pattern):
    first = list(index_seq(sorted(Seq)))
    last = list(index_seq(Seq))
    top = 0
    bottom = len(last) - 1
    LastFirstMap = {}
    #enumerate, i is the index where the (char,count) occur inside the list
    for i, (char, count) in enumerate(last):
        for j, (f_char, f_count) in enumerate(first):
            if char == f_char and count == f_count:
                LastFirstMap[i] = j
                break

    while top <= bottom:
        if Pattern:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            if symbol in [last[i][0] for i in range(top, bottom + 1)]:
                indices = [i for i in range(top, bottom + 1) if last[i][0] == symbol]
                TopInd = min(indices)
                BotInd = max(indices)
                top = LastFirstMap[TopInd]
                bottom = LastFirstMap[BotInd]
            else:
                return 0
        else:
            return bottom - top + 1

with open("C:/Users/B103040059/Downloads/dataset_30226_8.txt", 'r') as file:
    Text = file.read().strip().split("\n")
'''
Sample Input:
TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC

Sample Output:
2 1 1 0 1
'''
Seq = Text[0]
Pattern = Text[1].split(" ")
res = []
for i in Pattern:
    res.append(str(BWTMatching(Seq, i)))
print(" ".join(res))