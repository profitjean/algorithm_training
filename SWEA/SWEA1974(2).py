testcase = int(input())
for t in range(1,testcase+1):
    sudoku = []
    ans = []
    res = 1
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    for i in range(9):
        count = [0] * 10
        for k in range(9):
            count[sudoku[i][k]] += 1
        ans.append(count)

    for j in range(9):
        count = [0] * 10
        for k in range(9):
            count[sudoku[k][j]] += 1
        ans.append(count)

    for i in range(0,9,3):
        for j in range(0,9,3):
            count = [0] * 10
            for k in range(3):
                for l in range(3):
                    count[sudoku[j+k][i+l]] += 1
            ans.append(count)

    for i in range(27):
        for j in range(1,10):
            if ans[i][j] != 1:
                res = 0
    print('#{} {}'.format(t, res))

