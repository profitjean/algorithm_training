testcase = int(input())
for t in range(1, testcase+1):
    fly = []
    answer = 0
    N,M = map(int, input().split())
    for _ in range(N):
        fly.append(list(map(int, input().split())))
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum = 0
            for k in range(M):
                for l in range(M):
                    sum += fly[i+k][j+l]
            if sum > answer:
                answer = sum

    print('#{} {}'.format(t, answer))