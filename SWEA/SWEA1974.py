testcase = int(input())

for t in range(1,testcase+1):
    sudoku = []
    ans = 1
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    for i in range(9):
        sum = 0
        for j in range(9):
            sum += sudoku[i][j]
        if sum != 45:
            ans = 0
            break

    for i in range(9):
        sum = 0
        for j in range(9):
            sum += sudoku[j][i]
        if sum != 45:
            ans = 0
            break

    print('#{} {}'.format(t, ans))

