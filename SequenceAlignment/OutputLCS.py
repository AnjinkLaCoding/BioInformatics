import numpy as np

def LCSBAckTrack(v, w):
    S = np.empty((len(v) + 1, len(w) + 1))
    BackTrack = [[None for j in range(len(w) + 1)] for i in range(len(v) + 1)]
    for i in range(len(v) + 1):
        S[i][0] = 0
    for j in range(len(w) + 1):
        S[0][j] = 0
    for i in range(1,len(v)+1):
        for j in range(1, len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            S[i][j] = max(S[i-1][j], S[i][j-1], S[i-1][j-1] + match)
            if S[i][j] == S[i-1][j]:
                BackTrack[i][j] = "Down"
            elif S[i][j] == S[i][j-1]:
                BackTrack[i][j] = "Right"
            elif S[i][j] == S[i-1][j-1] + match:
                BackTrack[i][j] = "Diagonal"
    return BackTrack

def LCSOutput(BackTrack, v, w):
    i = len(v)
    j = len(w)
    LCS = ""
    while i > 0 and j > 0:
        if BackTrack[i][j] == "Down":
            i -= 1
        elif BackTrack[i][j] == "Right":
            j -= 1
        elif BackTrack[i][j] == "Diagonal":
            LCS = v[i-1] + LCS
            i -= 1
            j -= 1
    return LCS

with open('C:/Users/Matthew/Downloads/dataset_OutputLCS.txt', 'r') as file:
    line = file.readlines()
s = line[0].strip()
t = line[1].strip()
Backtrack = LCSBAckTrack(s,t)
res = LCSOutput(Backtrack, s, t)
print(res)
with open('C:/Users/Matthew/Downloads/Sol.txt', 'w') as f:
    f.write(res)