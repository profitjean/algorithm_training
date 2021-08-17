def find_num(i, start, end):
    if start > end:
        return 0
    m = (start+end) // 2
    if i == a[m]:
        return 1
    elif i > a[m]:
        return find_num(i, m+1, end)
    else:
        return find_num(i, start, m-1)

n = int(input())
a = list((map(int, input().split())))
a.sort()

m = int(input())
b = list((map(int, input().split())))

for i in b:
    start = 0
    end = n -1
    print(find_num(i, start, end))

