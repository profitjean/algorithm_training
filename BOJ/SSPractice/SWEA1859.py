
T = int(input())
# 뒤에서부터 거꾸로 접근
# 마지막원소를 max로 지정한뒤,
# 거꾸로탐색해서 max보다 큰 값이 있으면 새로 갱신
# 아닌 경우에는 이익 계산해서 누적시키기
for test_case in range(1, T+1):
    answer = 0
    case = int(input())
    cost = list(map(int, input().split()))
    max = cost[-1]
    for i in range(case-2, -1, -1):
        if cost[i] >= max:
            max = cost[i]
        else:
            answer += max - cost[i]
    print('#{} {}'.format(test_case, answer))