from collections import deque

n = int(input()) # 3
numbers = list(map(int, input().split())) # 3 4 5

add, sub, mul, div = map(int, input().split()) # 1 0 1 0

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    # 잊지말자. global 키워드로 해당 전역 변수 재선언하기
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now+numbers[i])
            # 3+4*5 연산 먼저 진행
            # min_value = 35, max_value = 35
            # 다음 연산을 위해 제거했던 부호값을 다시 원상복귀시켜주어야
            # 또 다른 재귀연산을 진행할 수 있는 것임 (3*4+5)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now-numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now*numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/numbers[i]))
            div += 1
dfs(1, numbers[0])
print(max_value)
print(min_value)

