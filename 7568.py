n = int(input())
people = []
for _ in range (n):
    w, h = map(int, input().split())
    people.append((w,h)) # 키와 몸무게 튜플로 입력
for i in people:
    rank = 1 # i가 (55,185)일때
    for j in people: # j로 경우의 수 비교
        if i[0] < j[0] and i[1] < j[1]:
            rank = rank + 1
    print(rank)