import sys
import heapq

case = int(sys.stdin.readline().rstrip())
for _ in range(case):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    priority = list(map(int, sys.stdin.readline().rstrip().split()))
    checkList = [0 for _ in range(N)]
    checkList[M] = 1
    count = 0
    while True:
        if priority[0] == max(priority):
            count = count + 1
            if checkList[0] != 1:
                del priority[0]
                del checkList[0]
            else:
                print(count)
                break
        else:
            priority.append(priority[0])
            checkList.append(checkList[0])
            del priority[0]
            del checkList[0]
