import sys
input = sys.stdin.readline
maximum = 0
result = 0
case = int(input())
for _ in range(case):
    n = int(input())
    triangle = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    maximum = (max(triangle[-1]))

    for k in triangle[-1]:
        if maximum == k:
            result = result + 1
    print(result)