import heapq
import sys
n = int(sys.stdin.readline())
heap = []
for i in range(n):
    case = int(sys.stdin.readline())
    if case == 0:
        if heap:
            print(heapq.heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [case, case])