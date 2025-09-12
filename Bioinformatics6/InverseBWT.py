from collections import defaultdict
# Yields each character with the occurrence number
def index_seq(seq):
    d = defaultdict(int)
    for c in seq:
        yield c, d[c]
        #Returns the character and its current occurrence count (0-indexed)
        #Second time seeing 'A': yields ('A', 1), then increments count to 2
        d[c] += 1

def InverseBWT(seq):
    first = list(index_seq(sorted(seq)))
    last = list(index_seq(seq))
    curr = ("$", 0)
    res = ""
    for _ in range(len(seq)):
        curr = first[last.index(curr)]
        res += curr[0]
    return res


with open("C:/Users/B103040059/Downloads/dataset_30225_10 (2).txt", 'r') as file:
    Text = file.read().strip()
'''
Sample Input:
TTCCTAACG$A

Sample Output:
TACATCACGT$
'''
res = InverseBWT(Text)
print(res)