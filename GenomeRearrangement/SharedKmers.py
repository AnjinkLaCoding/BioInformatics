def reverse_complement(seq):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(seq))

def shared_kmers(k, s1, s2):
    # Step 1: Store all k-mers of s2 in a dictionary
    kmers_s2 = {}
    for j in range(len(s2) - k + 1):
        kmer = s2[j:j+k]
        if kmer not in kmers_s2:
            kmers_s2[kmer] = []
        kmers_s2[kmer].append(j)
    
    # Step 2: Find matches with k-mers of s1 (and reverse complements)
    result = []
    for i in range(len(s1) - k + 1):
        kmer = s1[i:i+k]
        rev = reverse_complement(kmer)
        
        # Match forward
        if kmer in kmers_s2:
            for j in kmers_s2[kmer]:
                result.append((i, j))
        
        # Match reverse complement
        if rev in kmers_s2:
            for j in kmers_s2[rev]:
                result.append((i, j))
    
    return result

with open('C:/Users/Matthew/Downloads/dataset_30164_5.txt', 'r') as file:
    lines = file.readlines()
k = int(lines[0].strip())
s1 = lines[1].strip()
s2 = lines[2].strip()
print(k)
print(s1)
print(s2)
pairs = shared_kmers(k, s1, s2)
print(pairs)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    for i in pairs:
        f.write(f"{i}\n")