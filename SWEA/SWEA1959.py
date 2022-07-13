testcase = int(input())
for t in range(1,testcase+1):
    n,m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max = 0
    if n>m:
        n,m = m,n
        A,B = B,A
    for i in range(m-n+1):
        temp = 0
        for j in range(n):
            temp += A[j] * B[i+j]
        if temp > max:
            max = temp
    print("#{} {}".format(t, max))
