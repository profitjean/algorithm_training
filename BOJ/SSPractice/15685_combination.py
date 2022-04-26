from collections import deque
from itertools import  combinations

n, m = map(int, input().split())

house = []
chicken = []
square = []

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        result += temp
    return result

for i in range(n):
    square.append(list(map(int, input().split())))
    for j in range(n):
        if square[i][j] == 1:
            house.append((i,j))
        if square[i][j] == 2:
            chicken.append((i,j))

# 모든 치킨 집 중에서 m개를 뽑는 킹우의
candidates = list(combinations(chicken,m))
result = 1e9
print('x', candidates)
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)