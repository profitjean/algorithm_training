count = int(input()) #4
numbers = list(map(int, input().split())) # 2 3 5 7
res = 0


for i in numbers:
    c = 0
    for j in range(1, i+1): # i=2일때, j=1, j=2
        if i % j == 0: 
            c = c + 1 # c=2되면서 반복문 종료
    if c == 2: # 나눠지는 수가 1과 자기 자신만 있을 경우
        res = res + 1 # 소수이므로 카운트해주기
print(res)