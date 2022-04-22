n = int(input()) # 7일
t = []
p = []
max_value = 0
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x) # 3 5 1 1 2 4 2
    p.append(y) # 10 20 10 20 15 40 200

dp = [0] * (n+1)


for i in range(n-1,-1,-1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)