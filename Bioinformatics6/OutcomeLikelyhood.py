def forward_algorithm(sequence, alphabet, states, transition_matrix, emission_matrix):
    n = len(sequence)
    f = [{} for _ in range(n)]
    initial_prob = 1.0 / len(states)
    for k in states:
        f[0][k] = initial_prob * emission_matrix[k][sequence[0]]
    for i in range(1, n):
        x_i = sequence[i]
        for k in states:
            sum_transitions = 0
            for l in states:
                sum_transitions += f[i-1][l] * transition_matrix[l][k]
            f[i][k] = emission_matrix[k][x_i] * sum_transitions
    total_probability = sum(f[n-1][k] for k in states)
    return total_probability

input_file = open("C:/Users/Matthew/Downloads/dataset_30328_4.txt", 'r')
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
xzyyzzyzyy
--------
x y z
--------
A B
--------
	A	B
A	0.303	0.697 
B	0.831	0.169 
--------
	x	y	z
A	0.533	0.065	0.402 
B	0.342	0.334	0.324

Sample Output:
1.1005510319694847e-06
'''
res = forward_algorithm(sequence, alphabet, states, transition_matrix, emission_matrix)
print(res)