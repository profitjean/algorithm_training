# 청소년 상어
import copy

array = [[None]* 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j*2], data[j*2+1]-1]

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
result = 0


def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

# 모든 물고기를 회전시키고 이동시키는 함수
def move_fish(array, now_x, now_y):
    for i in range(1,17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            for j in range(8): # 이동할 수 없는 범위라면 반시계 방향으로 회전시켜주기
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0<= nx < 4 and 0<= ny < 4:
                    # (0,0)부터 (3,3)
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = (direction+1) % 8

def move_shark(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위내에 위치하는가?
        if 0<= now_x <4 and 0<= now_y <4:
            # 물고기가 존재한다
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions

def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1

    move_fish(array, now_x, now_y)

    positions = move_shark(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료한다
    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)
    # 물고기 이동
    # 반시계방향으로 돌리기
    # 상어 방향대로 물고기 섭취시키기, 해당 물고기 합 합쳐서 return시키기

dfs(array, 0,0,0)
print(result)