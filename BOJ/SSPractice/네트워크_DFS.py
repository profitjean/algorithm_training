from collections import deque


def solution(n, computers):
    def dfs(i):
        visited[i] = 1
        for a in range(n):
            if computers[i][a] == 1 and visited[a] == 0:
                dfs(a)

    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if visited[i] == 0:
            dfs(i)
            answer = answer + 1
    return answer