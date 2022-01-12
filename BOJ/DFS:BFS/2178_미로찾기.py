import sys
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

start = 1 # 전선길이 최솟값은 1
end = max(arr)

result = 0
while start <= end:
    total = 0  # 전선개수 카운팅
    mid = (start + end) // 2
    for i in arr:
        total = total + (i // mid)
    if total < m:
        # 전선개수가 더 작게 나왔다는건, 더 작게 나눠서 많이 나오게 해야함
        # 좀 더 적게 나누는 값은 좌측이니까 범위 왼쪽으로 이동
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(end)
