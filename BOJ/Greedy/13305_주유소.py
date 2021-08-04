city = int(input()) # 4
distance = list(map(int, input().split())) # 2 3 1
cost = list(map(int, input().split())) # 5 2 4 1

res = cost[0]
min_sum = 0
for i in range(len(distance)):
    if cost[i] < res:
        res = cost[i]
    min_sum = min_sum + (res * distance[i])

print(min_sum)