#Making skew diagram, initialize the diff as 0, whenever we encounter C we will subtract it by 1 (-1), for G we will add it by 1 (+1)
#skew i(i range from 0 to len(genome)) (genome), skew 0 = 0

def SkewDia(text):
    res = []
    Diff = 0
    for i in range(len(text)):
        res += [str(Diff)]
        if text[i]=='C':
            Diff -= 1
        elif text[i]=='G':
            Diff += 1
    res += [str(Diff)]
    return ' '.join(res)

Text = 'GAGCCACCGCGATA'
SkewRes = SkewDia(Text)
print(SkewRes)

# the answer is: 0 1 1 2 1 0 0 -1 -2 -1 -2 -1 -1 -1 -1