

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    view = 0
    # point. 주변 2개 건물이 조망권에 들어오는지 체크
    for i in range(2, n-2):
        p1 = building[i] - building[i-2]
        p2 = building[i] - building[i-1]
        p3 = building[i] - building[i+1]
        p4 = building[i] - building[i+2]
        if p1 > 0 and p2 > 0 and p3 > 0 and p4 > 0:
            view += min(p1,p2,p3,p4)

    print('#{} {}'.format(test_case, view))