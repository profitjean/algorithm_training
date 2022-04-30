from collections import deque


def solution(priorities, location):
    answer = 0
    flag = 0
    wait = deque(priorities)
    index = deque()

    for i in range(len(priorities)):
        index.append(i)

    while len(wait)>1:
        q = wait.popleft()
        i = index.popleft()
        if q < max(wait):
            wait.append(q)
            index.append(i)
        if i == location:
            break
    answer = flag
    return answer

'''
모범답안 : enumerate 사용해서 현재 대기순서의 인덱스 값 추출하기
'''

