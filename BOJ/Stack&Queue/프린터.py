from collections import deque


def solution(priorities, location):
    answer = 0
    flag = 0
    wait = deque(priorities)
    index = deque()

    for i in range(len(priorities)):
        index.append(i)

    while wait:
        q = wait.popleft()
        i = index.popleft()
        if q < max(wait):
            wait.append(q)
            index.append(i)
        if i == location:
            break
    answer = flag
    return answer