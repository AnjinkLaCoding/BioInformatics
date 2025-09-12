def PartialSuffix(Text, k):
    Suffix = []
    for i in range(len(Text)):
        Suffix.append((Text[i:], i))
    SuffixArr = sorted(Suffix, key = lambda x:x[0])
    Partial ={}
    for i, (text, val) in enumerate(SuffixArr):
        if val % k == 0:
            Partial[i] = val
    return Partial

with open("C:/Users/B103040059/Downloads/dataset_30234_2.txt", 'r') as file:
    Text = file.read().strip().split("\n")
'''
Sample Input:
PANAMABANANAS$
5

Sample Output:
1 5
11 10
12 0
'''
Seq = Text[0]
k = int(Text[1])
res = PartialSuffix(Seq, k)
for a, b in res.items():
    print(f"{a} {b}")
with open('C:/Users/B103040059/Downloads/Sol.txt', 'w') as f:
    for a, b in res.items():
        f.write(f"{a} {b}\n")