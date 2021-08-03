numbers = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
words = input()
time = 0 

for i in range(len(words)):
    for j in numbers:
        if words[i] in j:
            time = time + numbers.index(j) + 3
print(time)