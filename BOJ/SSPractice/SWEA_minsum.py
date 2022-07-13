def solution(x, y, sub_sum):
    global answer
    sub_sum += arr[x][y]

    if x == size-1 and y == size-1:
        if answer > sub_sum:
            answer = sub_sum
        return
    elif answer < sub_sum:
        return


    dx = [0, 1]
    dy = [1, 0]

    for i in range(2):
        hx, hy = dx[i], dy[i]
        nx = x + hx
        ny = y + hy
        if nx < size and ny < size:

            solution(nx,ny,sub_sum)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = 99999999999
    arr = []
    size = int(input())
    for _ in range(size):
        arr.append(list(map(int, input().split())))
    solution(0,0,0)

    print('#{} {}'.format(test_case, answer))