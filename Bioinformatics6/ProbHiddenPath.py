import re

with open("C:/Users/Matthew/Downloads/dataset_30326_8 (2).txt", 'r') as file:
    text = file.read()
'''
Sample Input:
ABABBBAAAA
--------
A B
--------
	A	B
A	0.377	0.623
B	0.26	0.74

Sample Output:
0.000384928691755
'''
numbers = [float(x) for x in re.findall(r'\d+\.\d+', text)]
path = text.strip().split('\n')[0]
transition = {
    'A': {'A': numbers[0], 'B': numbers[1]},
    'B': {'A': numbers[2], 'B': numbers[3]}
}
P = 0.5
for i in range(len(path)-1):
    P *= transition[path[i]][path[i+1]]
print(str("%.30f" % P))
