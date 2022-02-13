import heapq
def solution(jobs): #[[0, 3], [1, 9], [2, 6]]
    answer = 0
    end, i = 0, 0
    start = -1
    hq = []
    while len(jobs) > i:
        for job in jobs:
            if start< job[0] <= end:
                heapq.heappush(hq, (job[1], job[0])) # 3, 0
                print("hq", hq)
        if len(hq) > 0:
            now = heapq.heappop(hq)
            print("now", now)
            start = end
            print(start)
            end = end + now[0]
            print(end)
            answer = answer + (end-now[1])
            i = i + 1
        else:
            end = end + 1
    answer = answer // len(jobs)
    return answer
solution([[0, 3], [1, 9], [2, 6]])