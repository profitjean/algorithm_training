import sys

def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

switch_count = int(input())
switch = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    sex, number = map(int, input().split())
    if sex == 1:
        for i in range(number-1, switch_count, number):
            change(i)
            print('male',switch, i)
    else:
        count = number - 1
        double_count = count * 2
        if count > 0:
            change(count)
            for i in range(count-1, -1, -1):
                j = double_count - i
                if switch[i] == switch[j]:
                    change(i)
                    change(j)
                    
                    print('female',switch,i,j)
                else:
                    print('female',switch,i)
                    break
        else:
            change(i)

if switch_count <= 20:
    print(*switch)
else:
    for i in range(len(switch)):
        print(switch[i], end='')
        if i+1 >= 20 and (i+1)%20 == 0:
            print()
