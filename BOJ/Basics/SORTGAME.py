import sys
from collections import deque
input = sys.stdin.readline
def bfs(start, length):
    queue = deque()
    queue.append((start, 0))
    while queue:


case = int(input().rstrip()) #3, testcase
dp = {}
array = [str(num+1) for num in range(8)]
bfs(array, len(array))

for _ in range(case):
    n = int(input().rstrip()) #8
    array = list(map(int, input().rstrip().split())) # 1 2 3 4
    sorted_array = list(sorted(array))



