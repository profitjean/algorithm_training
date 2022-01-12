import sys
n, m = map(int, sys.stdin.readline().split())
a = list(map(int, input().split()))
a.sort()
# two pointer 전략
lt = 0
rt = n -1
while lt <= rt:
    mid = lt+rt//2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1