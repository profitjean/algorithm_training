case = int(input())
num = []
save = 0
for _ in range(case):
    num.append(int(input()))

for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i],num[j] = num[j], num[i]

for k in num:
    print(k)