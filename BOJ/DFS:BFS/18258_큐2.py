import sys
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push":
        value = word[1]
        q.append(value)
    elif order == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order == "size":
        print(len(q))
    elif order == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif order == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    

    