import sys
sys.setrecursionlimit(10**9)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if graph[x][y] == 1:
            graph[x][y] = 0
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
            return True
        return False

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                cnt += 1

    print(cnt)