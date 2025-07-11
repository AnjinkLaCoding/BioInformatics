#Function to map the k-mer words in the interval
def MappingKmers(text,k):
    Map = {}
    for i in range(len(text)-k+1):
        word = text[i:i+k]
        if word in Map:
            Map[word]+=1
        else:
            Map[word]=1
    return Map

#Function to return a set of k-mers with their occur frrequency is >= t
def findClump(k,L,t,text):
    Map = {}
    KmersWord = set()
    for i in range(len(text)-L+1):
        Map = MappingKmers(text[i:i+L],k)
        for key,freq in Map.items():
            if freq>=t:
                KmersWord.add(key)
    return KmersWord

Text = 'TTTGAACCTCCGTACATGGGCGCGTGAAGATTAAATGTGCACAAAGTCGACGGTACCGATGGCTAACGAACCTATCCCGGGCCAGGCGAATAGCGTGGGCCGTCTCGTGTGCTCTAGGCGATCCACGACTTTAGGCGATCCGCAACACGTAGGCGATCCATCGTTGCGCTATCCTTGATTAGGCGATCCCCGCCTGTAGGCGATCCCGATCCGGTCGGCCAGATCTTATGAGTCGAGCACTTCGACTGGGCCGGCCTTGAGTTTGTAGATTGCACGACCAGACTTGTAGGTTACACTTGGTTGGGTATTAACTCATTGTTTATTCTCATTGCTCATTGTTTTTTGCTCATTGTTTAGATGCTTTCGCGCATCCTCATTGTTTGAGCGTTCCGCACGTCGTGAGGAACTATAGACCTAATTATACTTTTTCTGCTCAGCCGCCAATAAAATAAGAGCCAGGGGCCAGTGGACAAGTAAACGTGCCGAACATTTGGGGAGATATCAAGGTCCTGAACGTGTATCAACTGACGTGTATCAATACCATGTTCCTGTCAACGGAACGTTGCATTGGGTTGGTTGCATTGGTTGCATTCCTATGCGTTCGCCTATGCGTTCCTATGCGTTGTTGCATTGGTCTAACCTCCTATGCGTTATTCGGCCACGCGATATAGTTACCTAAGGGGCTGCCACGCGATGCCCGCGCGCGCCACGCGATGGTGCCACGCGATACACGACACGATGGCACGATGGTATGGTACGGACTGACTCACGCACGATGGTAGCGGATTTATGATCCCAGAGGAATTGTAATGCTAGCTACGAAAGGAATACGGGTCATCAAAGACAAATATGGAGAGTTGGCGCTTACCGATATCAATATCTGGATTTATCTGGATTCTGGATTTTGTGGTTAATATCACTTATATATATCTGGATTTATTTACAACGATATCTGGTATCTGGATTGATTCTAACAGTCTACCCAACGAGTACAACGCAGTCAGTCTACCCCCCTATCGTTATCAGTCTACCCACAGTCTACCCGACCCCTACCCACCCCTATCGATCGCCCCTATCGGAACGTGTTGTCGTGTGGACCTCGTCTCGAACGTGTCCCTCGAACGTGTACCCTGGTCCTTGAATATCAAGATCTGCCGGCTAGTAAGTATCTTGGGTCAAGTGTTAGGGTCCACCTTTCACCCAACGTCATGCCTTGCACCCAGGGCTCTCCTGACCTTTATCCCACCCGGACTCATCAGAGCCGTAGCAATTTATGACTTGTCACTATCGTCTTTGCGTGATCGGTAGGATCTGTTAGATTCTCGGGAATGGGAGCAAATCTCCGTTTCCCGTCTAATCCCCCAAATACCAGCAAAGGGTACAATGGGCGGTGAACGCACACGAAAAACTTTAGTGCTTTCAGGCTTTCAGGTCTAGTGCTTTCAGCCTTGGCGTGCTTTCAGCGGTCTAGTGCTTTCGTGCTTAGGACAGGATGCAGTCAGGACAGGATAGAGGACAGGATGGACAGGATCTAGGACAGGATGGATTTCCCGGGGAAGGACAGGATGACAGGATATCTATCCCTCCCTCCCTCCCTATCCCTCCCATCCCTCCCTCGGCGTTATCCCTCCCTAGTTGGTCCGTCCCTTTGACTGTTAGACTTTGCCCTGAGTTCCAGTCTGCACCTAATGTGAGTCGTCCCTTTGACCCGTCCCTTTGATGATTTCTACTAGGGGATAGTTGACACTCTCGAGCTAAATGGACGGGAACTCTCGAGCAGCTGAACTCTCGACTCTCGAGCTCGAGCTCATCATACGCTAGCGTGGTGGACGCGCCGGAGGACGTTACTTAAGGCGCCTTTACAATTCGGTGGCATATAAAGTGGAGGCCCCTTGGGTCACGTGTGAGACAGCGAGATGATCCTGGTGTATTATTTCCATATAAATCTTTGGATACGGGCAGATTATCTGTAACCATCTCGGACGGTACGTCAGAGATTG'
res = findClump(10,100,4,Text)
res = ' '.join(res)
print(res)

#The result is : CCTATGCGTT TATCTGGATT GCCACGCGAT AGGACAGGAT TAGGCGATCC CAGTCTACCC CTCATTGTTT GGACAGGATG
