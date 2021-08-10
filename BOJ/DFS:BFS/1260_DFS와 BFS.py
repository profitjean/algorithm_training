import sys
from collections import deque
# 4 5 1
n,m,v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)] # 2차원 배열 생성하기
for _ in range(m):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()
# 방문 여부 저장하는 리스트 visited
visited = [False] * (n+1)
# 모든 노드를 방문하려고 할 때는 DFS
# 인접한 노드 중 숫자가 작은 노드를 선택하여 방문처리 이후 탐색 진행
def Dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        print(i)
        if not visited[i]:
            Dfs(graph, i, visited)
# 최단 경로 찾기
# 큐를 활용하는 BFS
# 노드를 큐에 삽입하고, 노드를 꺼내서 해당 노드의 인접 노드 중,
# 방문하지 않은 노드는 모두 큐에 삽입한다
def Bfs(graph, v, visited):
    visited = [False] * (n+1)
    queue = deque([v])
    visited[v] = True
    while queue:
        pop = queue.popleft()
        print(pop, end=' ')
        for i in graph[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
Dfs(graph, v, visited) # 2차원배열, 1, visited여부 배열
#print()
#Bfs(graph, v, visited)
