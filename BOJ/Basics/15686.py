# 삼성 기출
# 치킨 배달
import sys
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input())
chicken, house = [], []

for r in range(N):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken,m))
def get_sum(candidates):
    result = 0
    # 모든 집에 대하여 가장 가까운 치킨집 find (완전탐색)
    for x, y in house:
        temp = 1e9 # 졸라 큰 숫자 1e9
        for hx, hy in candidates:
            # 절댓값 abs 함
            temp = min(temp, abs(x-hx) + abs(y-hy))
        # 가장 가까운 치킨집까지의 거리를 plus
        result += temp
    return result

# 치킨 거리의 합의 minimum
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)



