n = int(input())
count = n

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word.find(word[i]) > word.find(word[i+1]):
            count -= 1
            break
print(count)