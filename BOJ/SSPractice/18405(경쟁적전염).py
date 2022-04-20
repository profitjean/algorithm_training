from collections import deque

n, k = map(int, input().split())
graph = [] # 전체 보드에 대한 정
data = [] # 바이러스에 대한 정보
temp = [[0] * n for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
            # print('바이러스종류', data)

# 정렬 이후 큐로 옮기기. 낮은 번호가 먼저 증식된다
data.sort()
q = deque(data) # 배열에 deque()로 감싸면 바로 큐로 옮기기 가넝

target_s, target_x, target_y = map(int, input().split())

dx = [-1,1,0,0]
dy = [0, 0,-1,1]

# 탐색
# 큐에 넣고 큐 기준으로 한바퀴씩 탐색을 진행하는구나
while q:
    # 큐가 빌때까지 while문 반복
    virus, s, x, y = q.popleft()
    # print('v, s, x, y', virus, s, x, y)
    # 정확히 s초가 지날때까지 while문 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인하기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 아직 방문하지 않은 위치라면
            if graph[nx][ny] == 0:
                # 그 위치에 바이러스를 넣는다
                graph[nx][ny] = virus
                # 시간 1초 증가시킨뒤 다시 큐 while 탐색 반
                q.append((virus, s+1, nx, ny))

print(graph[target_x-1][target_y-1])

