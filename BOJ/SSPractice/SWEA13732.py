
def check(board, cnt, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                down = 0
                right = 0
                for k in range(i+1,n):
                    if board[k][j] == 1:
                        down +=1
                    else:
                        break
                for k in range(j+1,n):
                    if board[i][k] == 1:
                        right += 1
                    else:
                        break

                if down != right:
                    return 'no'

                for x in range(i, i+down+1):
                    for y in range(j, j+right+1):
                        if board[x][y] == 1:
                            cnt -= 1
                        else:
                            return 'no'
                if cnt != 0:
                    return 'no'
                return 'yes'

testcase = int(input())
for t in range(1,testcase+1):
    answer = ''
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        data = list(map(str, input()))
        for j in range(n):
            c = data[j]
            if c == '#':
                board[i][j] = 1
                cnt += 1
            else:
                continue
    result = check(board, cnt, n)
    print('#{} {}'.format(t, result))


    # 이번달N월 ~ 내년 (N-1)월까지 납부금액의 총합 = 연간 납부금액
    # return
    # [이번달에는 vip가 아니지만 다음달에 vip가 되는 고객의 수,
    # 이번달에는 vip지만 다음달에 vip가 아니게 되는 고객의 수]
    # periods : 고객들의 가입 기간, [20, 23, 24]
    # pyaments: 고객들의 납부내역,
    # estimates: 납부예정금액
    def solution(periods, payments, estimates):
        answer = [0, 0]
        for i in range(len(periods)):
            per = periods[i]
            hap = sum(payments[i])
            if hap >= 900000 and per < 24:
                hap -= payments[i][0]
                hap += estimates[i]
                per += 1
                if hap >= 900000 and per >= 24:
                    answer[0] += 1
                    continue
            if hap >= 900000 and per >= 24:
                hap -= payments[i][0]
                hap += estimates[i]
                if hap < 900000:
                    answer[1] += 1
                    continue
            if hap < 900000 and per >= 24:
                hap -= payments[i][0]
                hap += estimates[i]
                if hap >= 900000:
                    answer[0] += 1
                    continue
            if hap >= 600000 and per >= 120:
                hap -= payments[i][0]
                hap += estimates[i]
                per += 1
                if hap >= 900000:
                    answer[1] += 1
                    continue
            if hap >= 600000 and per < 120:
                hap -= payments[i][0]
                hap += estimates[i]
                per += 1
                if per >= 120:
                    answer[0] += 1
                    continue

        return answer