import heapq
import sys

def solution(scoville, k):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    while heap[0] < k and len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        heapq.heappush(heap, num1+num2*2)
        answer = answer + 1
    if heap[0] >= k:
        return answer
    else:
        return -1


if __name__ == "__main__":
    print(solution([1,2,9,3,10,12],7))