count = int(input()) #4
numbers = list(map(int, input().split())) # 2 3 5 7
res = 0


for i in numbers:
    c = 0
    for j in range(1, i+1):
        if i % j == 0:
            c = c + 1
    if c == 2:
        res = res + 1
print(res)