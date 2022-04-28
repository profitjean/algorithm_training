from collections import deque
'''
현재 가고 있는 길이 가장 최소의 길이라는 보장
'''
INF = 1e9
# 졸라 큰 값.
# 값 변경여부같은거 확인할때 저장해놓기

n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

size = 2
shark_x, shark_y = 0, 0

for i in range(n):
    for j in range(n):
        # 현재 아기상어의 위치를 저장한
        if array[i][j] == 9:
            shark_x, shark_y = i, j
            array[shark_x][shark_y] = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    dist = [[-1]*n for _ in range(n)]
    # dist는 지나갈 수 있 여부를 저장하는 2차원배열
    # 값이 -1이면 지나가기 불가
    # 지나가기 가능하면 dist에도 값 새로 반영

    q = deque([(shark_x, shark_y)])
    dist[shark_x][shark_y] = 0
    while q:
        x, y = q.popleft()
        # 4방향 탐색 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n:
                # 자신의 크기보다 작거나 같은 경우에만 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= size:
                    # 아기상어 위치로부터 nx,ny까지의 최단거리를 누적시켜줍니다.
                    dist[nx][ny] = dist[x][y] + 1
                    # 방문처리
                    q.append((nx, ny))
    return dist

# 최단거리가 주어졌을때, 먹을 물고기를 탐색해보자
def find(dist):
    x, y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
           # 도달이 가능하고(최단거리로 지나가고), 섭취가능한 물고기인 경우(아기상보다 작은 크기의 물고기)
            if dist[i][j] != -1 and 1<= array[i][j] < size:
                # 가장 가까운 물고기 한마리만 선택하기 (위쪽, 그리고 왼쪽에 있을수록 우선인 물고기)
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return None
    else:
        return x,y, min_dist # 먹은 물고기의 좌표 x,y 최단거리 저장한 min_dist

result = 0 # 최종 답안으로 return 할 값
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치를 찾기
    # break로 탈출할때까지 계속 탐색 진행
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리를 출력한다
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신해주고, 이동거리도 새로 갱신해준
        shark_x, shark_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에서는 이제 아무것도 없도록 처리한다는
        # 그래야 while문 안에서 다음으로 먹을 물고기 찾으면서 최단거리 갱신이 가능한
        array[shark_x][shark_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        # 그니까 현재 사이즈가 2야. 사이즈 1 증가하려면 사이즈1짜리 물고기 2마리 먹어야한다는 말
        if ate >= size:
            size += 1
            ate = 0