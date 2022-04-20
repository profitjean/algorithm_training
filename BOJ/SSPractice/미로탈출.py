# bfs는 너비우선탐색, 모든 노드 탐색 순차적으로..
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동방향설정
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# BFS로 구현
def bfs(x, y):
    #bfs는 큐로 구현하기?
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        # 현 위치로부터 네 방향에서 위치 확인해보기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어난경우에는 무시하기
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록한다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[nx][ny] + 1
                queue.append((nx, ny))

    # 가장 오른쪽 아래까지의 최단 거리를 반환하기
    return graph[n-1][m-1]

# BFS를 수행한 결과를 출력
print(bfs(0,0))
