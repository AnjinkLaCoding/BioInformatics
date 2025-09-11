with open("C:/Users/Matthew/Downloads/dataset_30231_2.txt", 'r') as file:
    Text = file.read().strip()
'''
Sample Input:
AACGATAGCGGTAGA$

Sample Output:
15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
'''
Suffix = []
for i in range(len(Text)):
    Suffix.append((Text[i:], i))
SuffixArr = sorted(Suffix, key = lambda x:x[0])
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(" ".join([str(i[1]) for i in SuffixArr]))