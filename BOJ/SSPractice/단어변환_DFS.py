from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    visited = [0 for _ in words]

    q = deque()
    q.append([begin, 0])

    while q:
        print(q)
        x, count = q.popleft()
        if x == target:
            return count

        for i in range(0, len(words)):
            dif = 0
            word = words[i]

            for j in range(len(x)):
                if x[j] != word[j]:
                    dif += 1

            if dif == 1:
                if visited[i] == 1:
                    continue
                else:
                    visited[i] = 1
                q.append([word, count + 1])
    return count

'''
처음에는 hit
비슷한 다음 deque()에 hot. 탐색 진행시 
이미 탐색을 진행했던 hit과 다시 탐색을 진행하는건 불필요하니까
앞에서 만들었던 visited flag로 판단을 해주는것
'''
