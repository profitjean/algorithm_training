test = int(input())
trial = 0

while 1:
    a = test // 10 #6
    b = test % 10 #8
    c = (b*10) + ((a+b)%10) #8
    if c == test:
        break
    trial += 1
    a = b
    b = c
    
print(trial)
