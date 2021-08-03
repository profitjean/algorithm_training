count, cost = map(int, input().split())
coin = []
amount = 0
for _ in range(count):
    a = int(input())
    coin.append(a)
for i in range(len(coin)-1, -1, -1):
    if cost >= coin[i]:
        amount += cost // coin[i]
        cost = cost % coin[i]
print(amount)