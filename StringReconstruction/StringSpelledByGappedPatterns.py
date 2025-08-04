def StringSpelledByGappedPatterns(prefix, suffix, k, d):
    res = ""
    flag = 0
    for i in range(k + d, len(prefix)):
        if prefix[i] == suffix[i - k - d]:
            flag = 1
        else:
            flag = 0
    if flag == 1:
        res = prefix[:k+d] + suffix[:]
    return res

k = 0
d = 0
with open('C:/Users/Matthew/Downloads/dataset_30208_4.txt', 'r') as file:
    line = file.readlines()
k,d = line[0].strip().split(" ")
k = int(k)
d = int(d)
Text = line[1].strip().split(" ")
#print(Text)
prefix = ""
suffix = ""
for i in range(len(Text)):
    if i == 0:
        prefix += Text[i][:k]
        suffix += Text[i][k+1:]
    else:
        prefix += Text[i][k-1]
        suffix += Text[i][-1]
#print(prefix)
#print(suffix)
res = StringSpelledByGappedPatterns(prefix, suffix, k,d)
#print(res)
with open("C:/Users/Matthew/Downloads/solution.txt", "w") as file:
    file.write(res)