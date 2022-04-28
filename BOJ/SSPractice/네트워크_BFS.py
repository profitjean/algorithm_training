from collections import deque


def solution(n, computers):
    def BFS(i):
        q = deque()
        q.append(i)
        while q:
            i = q.popleft()
            visited[i] = 1
            for a in range(n):
                if computers[i][a] == 1 and visited[a] == 0:
                    q.append(a)

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if visited[i] == 0:
            BFS(i)
            answer = answer + 1
    return answer