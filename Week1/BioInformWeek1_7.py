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
    for i in range(L-k+1):
        if text[i:i+k] in Map:
            Map[text[i:i+k]]+=1
            if Map[text[i:i+k]] >= t:
                KmersWord.add(text[i:i+k])
        else:
            Map[text[i:i+k]]=1
    
    
    for i in range(1,len(text)-L+1):
        if text[i-1:i-1+k] in Map:
            Map[text[i-1:i-1+k]]-=1
        if text[i:i+k] in Map:
            #Map[text[i:i+k]]+=1
            if Map[text[i:i+k]] >= t:
                KmersWord.add(text[i:i+k])
        else:
            Map[text[i:i+k]]=1
        
        if text[i+L-k:i+L] in Map:
            Map[text[i+L-k:i+L]]+=1
            if Map[text[i+L-k:i+L]] >= t:
                KmersWord.add(text[i+L-k:i+L])
        else:
            Map[text[i+L-k:i+L]]=1
            
    return KmersWord


#We will now find the clump for E.Coli bacteria
# we use with open because the E-coli.txt is 4mb size and hell lot of characters, i nearly crash my laptop, ~4,641,652 characters
#Enter your path to the file E_coli.txt
with open('C:/Users/Matthew/Downloads/E_coli.txt', 'r') as file:
    Text = file.read().strip()
res = findClump(9,500,3,Text)
Kmers = ' '.join(res)
print(Kmers)
print(len(res))

# we got 1904 9-mers of (500,3)-clump for E.coli bacteria genome.
# the execution time is 8 seconds, and maybe can be optimize more
