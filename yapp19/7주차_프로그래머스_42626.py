import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        n1 = heapq.heappop(scoville)    
        if n1 >= K:
            return answer
        n2 = heapq.heappop(scoville)
        answer += 1
        heapq.heappush(scoville, n1 + n2 * 2)
    
    return -1 if len(scoville) == 0 or scoville[0] < K else answer
