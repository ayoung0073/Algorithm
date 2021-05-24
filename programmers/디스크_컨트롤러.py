import heapq
def solution(jobs):
    n = len(jobs)
    jobs.sort()
    q = []
    job_idx = 0 
    done = 0 # 처리 개수
    total = 0 # 총 걸린 시간
    
    while done < n:
        if not q: # 요청 들어온 것이 없는 경우, 가장 먼저 들어온 요청을 처리한다.
            request, time = jobs[job_idx]
            job_idx += 1
            current_time = request + time
            total += time
            
        else: # 요청 들어온 것이 있으면, 그것부터 처리
            time, request = heapq.heappop(q)
            current_time += time
            total += current_time - request
            
        done += 1
    
        # 요청 들어온 경우
        while job_idx < n and jobs[job_idx][0] <= current_time:
            heapq.heappush(q, jobs[job_idx][::-1])
            job_idx += 1
            
    return total // n
