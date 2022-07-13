testcase = int(input()) # 테스트케이스

for t in range(1,testcase+1):
    arr = []
    N = int(input())  # 사이즈 3
    for _ in range(N):
        arr.append(input().split())
    ans = [['']*3 for _ in range(N)]

    # [[1,2,3],[4,5,6],[7,8,9]]
    for i in range(N):
        for j in range(N):
            ans[i][0] += arr[N - 1 - j][i]
    ans[i][0] = int(ans[i][0])

    for i in range(N):
        for j in range(N):
            ans[i][1] += arr[N - 1 - i][N - 1 - j]
    ans[i][1] = int(ans[i][1])

    for i in range(N):
        for j in range(N):
            ans[i][2] += arr[j][N - 1 - i]
    ans[i][2] = int(ans[i][2])

    print('#{}'.format(t))
    for i in range(N):
        print(*ans[i])

