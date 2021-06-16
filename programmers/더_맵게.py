import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while True:
        min_scv = heapq.heappop(scoville)
        if min_scv >= K:
            break
        if not scoville:
            return -1
        answer += 1
        second_scv = heapq.heappop(scoville)
        heapq.heappush(scoville, min_scv + 2 * second_scv)
        
    return answer
