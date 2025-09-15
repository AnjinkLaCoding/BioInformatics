f = open("C:/Users/Matthew/Downloads/dataset_30326_10.txt", 'r')
data = f.read().split()
x = data[0]
path = data[6]
emission = {'A':{'x':float(data[-7]), 'y':float(data[-6]), 'z':float(data[-5])}, 'B':{'x':float(data[-3]), 'y':float(data[-2]), 'z':float(data[-1])}}
f.close()
'''
Sample Input:
zzzyxyyzzx
--------
x y z
--------
BAAAAAAAAA
--------
A B
--------
	x	y	z
A	0.176	0.596	0.228
B	0.225	0.572	0.203

Sample Output:
3.59748954746e-06
'''
P = 1
for i in range(len(x)):
    P *= emission[path[i]][x[i]]
print(str(f"{P:.11e}"))