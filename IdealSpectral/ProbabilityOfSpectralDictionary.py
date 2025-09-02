mass_table = [57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]

def SizeDict(Spectrum, threshold, maxScore):
    # Size[t][i] = number of peptides with mass i and score t
    Size = [[0.0] * (len(Spectrum) + 1) for _ in range(maxScore + 1)]
    
    Size[0][0] = 1.0

    for i in range(1, len(Spectrum) + 1):
        for t in range(maxScore + 1):
            for mass in mass_table:
                if i - mass >= 0:
                    score = t - Spectrum[i-1] 
                    if score >= 0 and score <= maxScore:
                        Size[t][i] += (Size[score][i - mass])/20
    result = 0.0
    for t in range(threshold, maxScore + 1):
        result += Size[t][len(Spectrum)]
    return result

with open("C:/Users/B103040059/Downloads/dataset_30266_8 (1).txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]
#The input is similar to below:
#4 -3 -2 3 3 -4 5 -3 -1 -1 3 4 1 3 - spectrum
#1 - threshold
#8 - max score
Spectrum = list(map(int, lines[0].split()))
threshold = int(lines[-2])
MaxScore = int(lines[-1])
result = SizeDict(Spectrum, threshold, MaxScore)
print(result)