import sys

cnt0 = [1, 0]
cnt1 = [0, 1] 

for i in range(2, 41):
    cnt0.append(cnt0[i-1]+cnt0[i-2])
    cnt1.append(cnt1[i-1]+cnt1[i-2]) 


case = int(sys.stdin.readline())
for _ in range(case):
    n = int(sys.stdin.readline())
    print(cnt0[n], cnt1[n])