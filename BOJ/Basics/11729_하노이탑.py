def hanoi_tower(n,start,middle,end):
    if n == 1:
        print(start,end)
    else:
        hanoi_tower(n-1,start,end,middle)
        print(start,end)
        hanoi_tower(n-1,middle,start,end)

n = int(input())
print(2**n -1)
hanoi_tower(n,1,2,3)