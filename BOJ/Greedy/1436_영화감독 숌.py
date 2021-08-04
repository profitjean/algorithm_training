n = int(input())
apocalypse = 666
count = 0
while True:
    if '666' in str(apocalypse):
        count = count + 1
    if count == n:
        print(apocalypse)
        break
    apocalypse = apocalypse + 1
    
        

