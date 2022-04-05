import sys
input = sys.stdin.readline

size = int(input())
student_list = []
table_list = [[0 for _ in range(size)] for _ in range(size)]
dic = {}
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(size **2):
    student_list.append(list(map(int, input().split(' '))))

def count(f_list, i, j):
    count = 0
    f_count = 0
    return

for s in student_list:
    friend = []
    for i in range(1,5):
        if s[i] in dic:
            friend.append(s[i])
            
    if friend:
        # 좋아하는 친구가 자리를 잡았다.
        # 자리탐색 all
        # 주변에 친한친구수, 근처 비어있는 곳 개수, i, j좌표
        max_cnt = []
        for i in range(n):
            for j in range(n):
                if table_list[i][j] == 0:
                    result, f_cnt = count(friend, i, j)
                    if not max_cnt:
                        max_cnt = [f_cnt, result, i, j]
                    
        
            