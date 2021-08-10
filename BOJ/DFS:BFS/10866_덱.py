import sys
from collections import deque

n = int(input())
q = deque()

for _ in range(n):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push_front":
        value = word[1]
        q.appendleft(value)
    elif order == "push_back":
        value = word[1]
        q.append(value)
    elif order == "pop_front":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif order == "pop_back":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
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

