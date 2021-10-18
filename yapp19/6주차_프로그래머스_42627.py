import heapq
def solution(jobs):
    n = len(jobs)
    jobs.sort() # 들어온 순서로 정렬
    q = []
    job_idx = 0 
    done = 0 # 처리 개수
    total = 0 # 총 걸린 시간
    
    while done != n:
        if not q: # 요청 들어온 것이 없는 경우, 가장 먼저 들어온 요청을 처리한다.
            start_time, time = jobs[job_idx]
            job_idx += 1 
            current_time = start_time + time
            total += time
            
        else: # 요청 들어온 것이 있으면, 그것부터 처리
            time, start_time = heapq.heappop(q)
            current_time += time
            total += current_time - start_time
            
        done += 1
    
        # 요청 들어온 경우
        while job_idx < n and jobs[job_idx][0] <= current_time: # job이 들어온 시각이 현재 작업 마친 시간보다 빠른 경우
            heapq.heappush(q, jobs[job_idx][::-1]) # jobs의 소요 시간이 빠른 것부터 처리해야함 -> [::-1]
            job_idx += 1
            
    return total // n
