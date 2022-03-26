import sys
input = sys.stdin.readline

n,m = map(int, input().split())
data = []
temp = [[0] * m for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))

# 상 우 하 좌
dx = [0, 0, 1, -1]
dy = [1, -1, 0 , 0]

result = 0

def virus(x,y):
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i] 
        # 상하좌우 중에서 바이러스가 퍼질 수 있는 케이스
        # 2차원 배열 범위 안에는 위치해야하니까
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                #바이러스 재배치
                temp[nx][ny] == 2
                virus(nx,ny)

def get_score():
    # 안전 영역의 크기 계산하는 메서드
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    # 울타리 3개 설치
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 바이러스의 위치 내에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        # 안전 영역의 최댓값계산하기
        result = max(result, get_score())
        return
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1
    
dfs(0)
print(result)