num = int(input())
n = 2

while True:
    if num % n == 0:
        print(n)
        num = num // n
    elif num == 1:
        break
    else:
        n = n + 1
