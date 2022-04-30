n = int(input())

data = []
teacher = []
wall = []
result = "NO"

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    data.append(list(map(str, input().split())))
    for j in range(n):
        if data[i][j] == 'T':
            teacher.append((i, j))

# 같은 선상에 선생님이 있으면 발각된다는 것이 포인트임
def check_t():
    global teacher, data
    for t in teacher:
        for i in range(4):
            x, y = t
            while 0 <= x < n and 0 <= y < n:
                if data[x][y] == 'O':
                    break # 장애물 발견시에는 while문 탈출
                elif data[x][y] == 'S':
                    return False # 학생 발견 시에는 발각되니까 False로 return
                x += dx[i]
                y += dy[i]
    return True

def dfs(count):
    global teacher, data, result, wall
    if count > 3:
        return
    if count == 3:
        if check_t() is True:
            result = "YES"
            return
        else:
            result = "NO"
    # n*n 2차원맵에서 탐색을 진행한다. 장애물의 개수가 3개에 도달할때까지
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X': # 아무것도 없는 부분이라면
                data[ i][j] = 'O' # 장애물을 배치시켜보면서 탐색
                dfs(count + 1)
                if result == "YES":
                    return
                data[i][j] = 'X' # 장애물 배치 후 다시 되돌려놓는과정은 필수


dfs(0)
print(result)