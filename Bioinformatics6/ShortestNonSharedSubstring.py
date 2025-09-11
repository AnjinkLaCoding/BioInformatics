def brute_force_solution(text1, text2):
    # Try all possible substring lengths starting from 1
    for length in range(1, len(text1) + 1):
        for i in range(len(text1) - length + 1):
            substr = text1[i:i + length]
            if substr not in text2:
                return substr
    return None  # All substrings of text1 appear in text2

with open("C:/Users/Matthew/Downloads/dataset_30222_7.txt", 'r') as file:
    Lines = file.read().strip().split('\n')
text1 = Lines[0]
text2 = Lines[-1]
res = brute_force_solution(text1, text2)
print(res)