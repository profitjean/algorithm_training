testcase = int(input())
for t in range(1,testcase+1):
    N,K = map(int, input().split())
    arr = []
    result = []
    answer = 0
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    for i in range(N):
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)

    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 1:
                count += 1
            else:
                result.append(count)
                count = 0
        result.append(count)

    for n in range(len(result)):
        if result[n] == K:
            answer += 1

    print('#{} {}'.format(t, answer))
