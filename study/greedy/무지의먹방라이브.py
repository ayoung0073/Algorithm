import heapq

def solution(food_times, k):

    # 전체 음식을 먹는 시간보다 k가 크거나 같으면 -1  # 더이상 섭취해야 할 음식이 없는 경우
    if sum(food_times) <= k:
        return -1
    
    length = len(food_times)
    
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i + 1)) # 시간 순으로 정렬될 것임
    
    sum_time = 0 # 먹기 위해 사용한 시간(현재까지)
    prev_time = 0 # 직전에 다 먹은 음식 시간
    
    while sum_time + ((q[0][0] - prev_time) * length) <= k: # 조건 체크
        now = heapq.heappop(q)[0]
        # print(prev_time, now, sum_time)
        sum_time += (now - prev_time) * length
        length -= 1 # 다 먹은 음식 제외
        prev_time = now # 이전 음식 시간 재 설정

    result = sorted(q, key = lambda x:x[1]) # 음식 번호 기준으로 정렬
    # print(result)
    return result[(k - sum_time) % length][1]
