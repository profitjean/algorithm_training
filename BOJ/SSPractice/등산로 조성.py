
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def dfs(x, y, cut):
    global MAX, visited
    MAX = max(MAX, visited[x][y])
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
            continue
        if square[x][y] > square[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, cut)
            visited[nx][ny] = 0
        elif cut and square[nx][ny] - k < square[x][y]:
            # 깎았을때 등산로 연결이 되는 경우
            temp = square[nx][ny]
            square[nx][ny] = square[x][y] - 1
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, cut -1) # 재귀적으로 k만큼 깎으면서 등산로 연결이 가능한지 탐색하게 되는
            # 다시 원상복귀 시켜줘야
            visited[nx][ny] = 0
            square[nx][ny] = temp

t = int(input())

for tc in range(t):
    n, k = map(int, input().split())
    square = []
    top = 0
    for i in range(n):
        square.append(list(map(int, input().split())))
        for j in range(n):
            if square[i][j] > top:
                top = square[i][j] # 최댓값

    MAX = 0
    visited = [[0] * n for _ in range(n)] # 전체 0으로 만든 2차원배열 만들어주기
    for i in range(n):
        for j in range(n):
            if square[i][j] == top: # 시작점 잡아주기
                visited[i][j] = 1
                dfs(i,j,1)
                visited[i][j] = 0

    print("#{} {}".format(tc+1, MAX))



