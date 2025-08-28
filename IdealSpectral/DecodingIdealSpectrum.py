from collections import defaultdict
import copy

AminoAcid = {57:"G",71:"A",87:"S",97:"P",99:"V",101:"T",103:"C",113:"L",114:"N",115:"D",128:"Q",129:"E",131:"M",137:"H",147:"F",156:"R",163:"Y",186:"W"}
AminoAcidRev = {"G":57,"A":71,"S":87,"P":97,"V":99,"T":101,"C":103,"I":113,"L":113,"N":114,"D":115,"K":128,"Q":128,"E":129,"M":131,"H":137,"F":147,"R":156,"Y":163,"W":186}

def Graph(Spectrum):
    res = defaultdict(list)
    Spectrum = [0] + Spectrum
    for i in range(len(Spectrum)):
        for j in range(i+1, len(Spectrum)):
            if Spectrum[j] - Spectrum[i] in AminoAcid:
                res[Spectrum[i]].append([Spectrum[j], AminoAcid[Spectrum[j] - Spectrum[i]]])
    return res

def CountPeptide(peptide):
    res = 0 
    for i in peptide:
        if i in AminoAcidRev:
            res += AminoAcidRev[i]
    return res

def IdealSpectrum(Peptide):
    res = []
    res.append(0)
    for i in range(len(Peptide)):
        if i == len(Peptide)-1:
            res.append(CountPeptide(Peptide[0:]))
            return sorted(res)
        prefix = Peptide[0:i+1]
        suffix = Peptide[len(Peptide)-i-1:]
        res.append(CountPeptide(prefix))
        res.append(CountPeptide(suffix))

def DecodingIdealSpectrum(Spectrum):
    GraphSpectrum = Graph(Spectrum)
    #print(GraphSpectrum)
    while GraphSpectrum[0]:
        path = GraphSpectrum[0][0][1]
        curr = GraphSpectrum[0][0][0]
        #print(f"First insertion is {path} currently on {curr}")
        GraphSpectrum[0].remove([curr, path])
        while True:
            temp = curr
            for i in GraphSpectrum[curr]:
                path += i[1]
                curr = i[0]
                GraphSpectrum[temp].remove(i)
                break
            #print(GraphSpectrum)
            #print(f"Sekarang curr ke {curr}")
            if curr not in GraphSpectrum:
                #print(f"{curr} is not in Graph")
                break
        #print(f"Now path is {path}")
        if IdealSpectrum(path) == Spectrum:
            #print("The path is right")
            break
    return path

with open("C:/Users/Matthew/Downloads/dataset_DecodingIdealSpectrum.txt", "r") as f:
    Spectrum = list(map(int, f.read().split()))
Spectrum.insert(0,0)
res = DecodingIdealSpectrum(Spectrum)
print(res)