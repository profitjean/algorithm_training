import sys

case = int(sys.stdin.readline())
hap = []
for _ in range(case):
    num = int(sys.stdin.readline())
    if num != 0:
        hap.append(num)
    else:
        hap.pop()
if len(hap) == 0:
    print(0)
else:
    print(sum(hap))
