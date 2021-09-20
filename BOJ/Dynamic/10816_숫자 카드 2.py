import sys

count = int(sys.stdin.readline()) #10
card = list(map(int, sys.stdin.readline().split())) # 6 3 2 10 10 -10 -10 7 3

dictList = dict() # 딕셔너리를 활용하여 key-value 타입으로 저장하기

for i in card: 
    if i in dictList:
        dictList[i] += 1 # 이후에 중복되어 다시 등장하면 1씩 더해주는 것
    else:
        dictList[i] = 1 # 처음 등장하면 1
# key값에는 카드의 값, value에는 해당 값이 몇 번 반복되는지 카운팅되어 저장
find = int(sys.stdin.readline()) #8
case = list(map(int, sys.stdin.readline().split())) # 10 9 -5 2 3 4 5 -10

for i in case: # 숫자카드를 딕셔너리와 비교하여 존재하면 앞서 만든 딕셔너리의 value 값을 출력해준다.
    if i in dictList:
        print(dictList[i], end=' ') 
    else:
        print(0, end=' ')



