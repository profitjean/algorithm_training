import sys

computer = int(sys.stdin.readline())
pair = int(sys.stdin.readline())
dictionary = {} # 키-값 저장하는 딕셔너리 사용
for i in range(1,computer+1):
    dictionary[i] = set() # 노드는 1번부터
for j in range(pair): 
    n1, n2 = map(int, sys.stdin.readline().split())
    dictionary[n1].add(n2)
    dictionary[n2].add(n1)

def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dictionary)
print(len(visited)-1) 
