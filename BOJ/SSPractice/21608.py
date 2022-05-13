# 상어초등학교

n = int(input())

info = []
info_dic = {}
for _ in range(n ** 2):
    a, b, c, d, e = map(int, input().split())
    info.append([a, [b, c, d, e]]) # 해당 학생 정보, [해당 학생이 좋아하는 학생에 대한 리스트들]
    info_dic[a] = [b, c, d, e] # 좋아하는 학생에 대한 정보는 딕셔너리에 넣어주기..

# print(info)

board = [list(0 for _ in range(n)) for _ in range(n)]

# print(board)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 1. 좋아하는 학생이 많은 칸
def favorite(student, friend):
    # student가 좋아하는 학생 리스트 - friend
    #   print(student, friend)
    count = [list(-1 for _ in range(n)) for _ in range(n)]
    max_chk = -1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:  # 해당 칸에 자리가 있다면
                chk = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    if 0 <= x < n and 0 <= y < n and board[x][y] in friend:  # 상하좌우에 친구가 있는 수 체크
                        chk += 1
                count[i][j] = chk
                max_chk = max(chk, max_chk)

    result = []

    # count결과에서 친구가 가장 많은 칸 탐색
    for i in range(n):
        for j in range(n):
            if count[i][j] == max_chk:
                result.append((i, j))

    return result


# 2. 인접한 칸 중에서 비어있는 칸이 많은 칸
def empty(result):
    # print("result", result)
    max_chk = -1
    count = [list(-1 for _ in range(n)) for _ in range(n)]

    for i in range(n):
        for j in range(n):

            if (i, j) in result:
                chk = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    if 0 <= x < n and 0 <= y < n and board[x][y] == 0:
                        chk += 1
                count[i][j] = chk
                max_chk = max(chk, max_chk)

    result2 = []

    # count결과에서 빈 칸이 가장 많은 칸 탐색
    for i in range(n):
        for j in range(n):
            if count[i][j] == max_chk:
                result2.append((i, j))

    result2.sort()
    return result2


# 학생의 만족도 계산
def cal():
    ans = 0
    for i in range(n):
        for j in range(n):

            chk = 0
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if 0 <= x < n and 0 <= y < n and board[i][j] != 0:
                    if board[x][y] in info_dic[board[i][j]]:
                        chk += 1

            if chk > 0:
                ans += 10 ** (chk - 1)
    return ans


for inf in info:
    rlt1 = favorite(inf[0], inf[1:][0])

    if len(rlt1) > 1:
        rlt2 = empty(rlt1)
        mx, my = rlt2[0][0], rlt2[0][1]
    else:
        mx, my = rlt1[0][0], rlt1[0][1]

    board[mx][my] = inf[0]

print(cal())