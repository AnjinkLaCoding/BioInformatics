AminoAcid = {57:"G",71:"A",87:"S",97:"P",99:"V",101:"T",103:"C",113:"L",114:"N",115:"D",128:"Q",129:"E",131:"M",137:"H",147:"F",156:"R",163:"Y",186:"W"}

def Graph(Spectrum):
    res = []
    Spectrum = [0] + Spectrum
    for i in range(len(Spectrum)):
        for j in range(i+1, len(Spectrum)):
            if Spectrum[j] - Spectrum[i] in AminoAcid:
                res.append(f"{Spectrum[i]}->{Spectrum[j]}:{AminoAcid[Spectrum[j] - Spectrum[i]]}")
    return res





with open("C:/Users/Matthew/Downloads/dataset_ConstructGraphSpectrum.txt", "r") as f:
    Spectrum = list(map(int, f.read().split()))
Edge = Graph(Spectrum)
for i in Edge:
    print(i)
