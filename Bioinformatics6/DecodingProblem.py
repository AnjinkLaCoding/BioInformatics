def viterbi_algorithm(sequence, alphabet, states, transition_matrix, emission_matrix):
    n = len(sequence)
    num_states = len(states)
    s = [{} for _ in range(n)]
    backtrack = [{} for _ in range(n)]
    initial_prob = 1.0 / num_states
    for k in states:
        s[0][k] = initial_prob * emission_matrix[k][sequence[0]]
        backtrack[0][k] = None  # No previous state for first position
    for i in range(1, n):
        x_i = sequence[i]  # Current observed symbol
        for k in states:  # Current state k
            best_score = 0
            best_prev_state = None
            for l in states:
                score = (s[i-1][l] * transition_matrix[l][k] * emission_matrix[k][x_i])
                if score > best_score:
                    best_score = score
                    best_prev_state = l
            s[i][k] = best_score
            backtrack[i][k] = best_prev_state
    best_final_score = 0
    best_final_state = None
    for l in states:
        if s[n-1][l] > best_final_score:
            best_final_score = s[n-1][l]
            best_final_state = l
    path = []
    current_state = best_final_state
    
    # Build path from end to beginning
    for i in range(n-1, -1, -1):
        path.append(current_state)
        current_state = backtrack[i][current_state]
    path.reverse()
    return ''.join(path)

input_file = open("C:/Users/Matthew/Downloads/dataset_30327_7.txt", 'r')
input_text = input_file.read()
input_file.close()
lines = input_text.strip().split('\n')

sequence = lines[0].strip()

separator_indices = [i for i, line in enumerate(lines) if line.strip() == '--------']

alphabet = lines[separator_indices[0] + 1].strip().split()

states = lines[separator_indices[1] + 1].strip().split()

transition_start = separator_indices[2] + 1
transition_matrix = {}

for i in range(transition_start + 1, transition_start + 1 + len(states)):
    parts = lines[i].strip().split()
    from_state = parts[0]
    transition_matrix[from_state] = {}
    for j, to_state in enumerate(states):
        transition_matrix[from_state][to_state] = float(parts[j + 1])

emission_start = separator_indices[3] + 1
emission_matrix = {}

for i in range(emission_start + 1, emission_start + 1 + len(states)):
    parts = lines[i].strip().split()
    state = parts[0]
    emission_matrix[state] = {}
    for j, symbol in enumerate(alphabet):
        emission_matrix[state][symbol] = float(parts[j + 1])
'''
Sample Input:
xyxzzxyxyy
--------
x y z
--------
A B
--------
	A	B
A	0.641	0.359
B	0.729	0.271
--------
	x	y	z
A	0.117	0.691	0.192	
B	0.097	0.42	0.483

Sample Output:
AAABBAAAAA
'''
res = viterbi_algorithm(sequence, alphabet, states, transition_matrix, emission_matrix)
print(res)