def ReadPair(k, d, text):
    res = []
    T1 = ""
    T2 = ""
    for i in range(len(text) - ((2*k) +d) + 1):
        T1 = text[i:i+k]
        T2 = text[i+k+d:i+(2*k)+d]
        res += [f"{T1}|{T2}"]
    return res

Text = "TAATGCCATGGGATGTT"
k = 3
d = 2
res = ReadPair(k,d,Text)
res.sort()
str = ""
for i in res:
    str += f"({i}) "
print(str)