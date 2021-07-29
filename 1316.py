n = int(input())
count = n

for i in range (0,n):
    word = input()
    for j in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                count = count -1

print(count)