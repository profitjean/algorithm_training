case = int(input())
count = 0
arr = []
result = []
temp = True
for _ in range(case):
    ret = int(input())
    while count < ret:
        count = count + 1
        arr.append(count)
        result.append("+")
    if arr[-1] == ret:
        arr.pop()
        result.append("-")
    else:
        temp = False
        break
if temp == False:
    print("NO")
else:
    for i in result:
        print(i)