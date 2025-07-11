#Function to find whihc position the pattern occur on the text
def findPattern(text,pattern):
    Pos=[]
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            Pos+=[str(i)]
    return Pos

with open('C:/Users/Matthew/Downloads/Vibrio_cholerae.txt', 'r') as file:
    Text = file.read().strip()
Patt = 'CTTGATCAT'
res = findPattern(Text,Patt)
res = ' '.join(res)
print(res)

#We got CTTGATCAT at positions: 60039 98409 129189 152283 152354 152411 163207 197028 200160 357976 376771 392723 532935 600085 622755 1065555
# we got ATGATCAAG at positions: 116556, 149355, 151913, 152013, 152394, 186189, 194276, 200076, 224527, 307692, 479770, 610980, 653338, 679985, 768828, 878903, 985368
# we can see that ATGATCAAG and CTTGATCAT is each others reverse complement, so they are basically two strands that suppose to be connected
#On CTTGATCAT there is 3 k-mers that located on a short interval between each others: 152283 152354 152411
#It is the same for ATGATCAAG: 151913, 152013, 152394
# So, we can conclude that maybe ATGATCAAG/CTTGATCAT is a replication origin, but we not sure yet.
