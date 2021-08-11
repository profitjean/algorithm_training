import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
circle = deque()
answer = []
num = 0

for i in range(1,n+1):
    circle.append(i)

while len(circle) != 0:
    for i in range(k):
        pick = circle.popleft() 
        circle.append(pick)
    answer.append(circle.pop())
print('<'+', '.join(map(str, answer)) + '>')

    
