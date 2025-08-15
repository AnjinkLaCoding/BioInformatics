def DPChange(money, Coins):
    MinNumCoins = [0] + [float('inf')] * money
    for i in range(1, money+1):
        for j in Coins:
            if i >= j:
                if MinNumCoins[i-j] + 1 < MinNumCoins[i]:
                    MinNumCoins[i] = MinNumCoins[i-j] + 1
    return MinNumCoins[money]

with open('C:/Users/Matthew/Downloads/dataset_30195_10 (1).txt', 'r') as file:
    line = file.readlines()
Money =int(line[0].strip())
coins = list(map(int, line[1].split()))
coins.sort()
res = DPChange(Money, coins)
print(res)