from collections import deque
import heapq
def solution(operations):
    answer = []
    q = []
    for op in operations:
        cal, num = op.split()
        num = int(num)
        if cal == 'I':
            heapq.heappush(q, num)
        else:
            if q:
                if num == -1: 
                    heapq.heappop(q)
                else:
                    data = max(q)
                    q.remove(data)

    if not q:
        answer = [0, 0]
    else:
        answer.append(max(q))
        answer.append(q[0])
        
    return answer
