# 마법사 상어와 복제
# 물고기 수 M, 상어가 마법을 연습한 횟수 S
# 격자 크기 4

from copy import deepcopy
from collections import deque

M, S = map(int, input().split())
# 리스트 만들어주기
smell = [[0]*4 for _ in range(4)]
fish = [[[] for _ in range(4)] for _ in range(4)]
# 물고기 이동 경로 (상하좌우, 대각선)
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
# 상어 이동 경로 (상하좌우)
s_dx = [-1, 0, 1, 0]
s_dy = [0, -1, 0, 1]

for _ in range(M):
    x, y, d = map(int, input().split()) # 물고기 위치
    fish[x-1][y-1].append(d-1)  # 배열 인덱스 넘버는 0부터 시작한다는것 잊지말기

shark_x, shark_y = map(int, input().split())
shark_x -= 1
shark_y -= 1


# TODO 상어 연속 3칸 이동
def move_shark(x,y,cnt, del_fish, direction, check):
    global  max_del, move_dir
    if cnt == 3:
        if del_fish > max_del:
            move_dir = deepcopy(direction)
            max_del = del_fish
        return

    for d in [2,0,6,4]:
        nx, ny = x + dx[d], y + dy[d]
        if not 0 <= nx < 4 or not 0 <= ny < 4:
            continue
        flag = 0
        if [nx, ny] in check:
            flag = 1
        if flag == 0:
            del_fish += len(fish[nx][ny])
        if fish[nx][ny]:
            check.append([nx, ny])
        cnt += 1
        direction.append(d)

        move_shark(nx, ny, cnt, del_fish, direction, check)

        if flag == 0:
            del_fish -= len(fish[nx][ny])
        if fish[nx][ny]:
            check.pop()
        cnt -= 1
        direction.pop()

# TODO 복제
for k in range(1,S+1):
    # deepcopy로 이전위치 복사시켜놓기
    fish_before = deepcopy(fish)
    fish_temp = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if fish[i][j]: # 현재 위치에 물고기가 있다
                for d in fish[i][j]:
                    flag = 0
                    for _ in range(8):
                        nx, ny = i + dx[d], j + dy[d]
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            if not (nx == shark_x and ny == shark_y):
                                # 이동 제약 안받고, 냄새도 안난다면, 방향 append 해주고 flag값 변경
                                if smell[nx][ny] == 0:
                                    fish_temp[nx][ny].append(d)
                                    flag = 1
                                    break
                        d = (d+7) % 8 # 범위가 적합하지 않다면, 방향 반시계 방향으로 돌리기
                    # 방향 탐색 반복문을 거쳤는데도 flag 값이 0이라면 이동 불가능하다는 뜻.
                    # fish_temp에 다시 append 시켜주자
                    if flag == 0:
                        fish_temp[i][j].append(d)
    fish = fish_temp

    max_del = -1
    move_shark(shark_x, shark_y, 0,0, deque(), deque())

    x,y = shark_x, shark_y
    for d in move_dir:
        nx, ny = x+dx[d], y+dy[d]
        if fish[nx][ny]:
            fish[nx][ny] = []
            smell[nx][ny] = k
        x, y = nx, ny
    shark_x, shark_y = x, y

    for i in range(4):
        for j in range(4):
            if smell[i][j] > 0:
                if k - smell[i][j] == 2:
                    smell[i][j] = 0

    for i in range(4):
        for j in range(4):
            if fish_before[i][j]:
                for d in fish_before[i][j]:
                    fish[i][j].append(d)

ans = 0
for i in range(4):
    for j in range(4):
        ans += len(fish[i][j])
print(ans)


