t = int(input())
test = []
for i in range (t):
    num, repeat = input().split()
    text = ""
    for j in repeat:
        text = text + int(num) * j
    print(text)