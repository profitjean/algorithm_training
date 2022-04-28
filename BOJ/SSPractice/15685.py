from collections import deque

def solution(idx, cnt):
    global ans
    if idx > len(chicken):
        return
    if cnt == m:
        s = 0
        for dx, dy in house:
            d = 1e9
            for i in value:
                cx, cy = chicken[i]
                d = min(d, abs(dx-cx) + abs(dy-cy))
            s += d
        ans = min(ans, s)
        return
    value.append(idx)
    print('value1', value)
    solution(idx+1, cnt+1)
    value.pop()
    print('value2', value)
    solution(idx+1, cnt)


n, m = map(int, input().split())
square = []
house = []
chicken = []
value = []
ans = 1e9

for i in range(n):
    square.append(list(map(int, input().split())))
    for j in range(n):
        if square[i][j] == 1:
            house.append((i,j))
        if square[i][j] == 2:
            chicken.append((i,j))

solution(0,0)
print(ans)