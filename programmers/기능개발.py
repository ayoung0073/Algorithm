from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    day = []
    for i in range(n):
        if (100-progresses[i]) % speeds[i] == 0: 
            day.append((100-progresses[i]) // speeds[i])
        else:
            day.append((100-progresses[i]) // speeds[i] + 1)
    
    q = deque(day)
    
    now = q.popleft()
    cnt = 1
    while q:
        comp = q.popleft()
        if comp <= now:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            now = comp
    
    answer.append(cnt)
            
    return answer
