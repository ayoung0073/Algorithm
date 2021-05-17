def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n
    # 대상 : 검색 시간의 범위
    while left <= right: 
        mid = (right + left) // 2 
        temp = n 
        for time in times: 
            temp -= mid // time
            if temp <= 0: 
                answer = mid 
                right = mid - 1 
                break 
        if temp > 0: # n명을 모두 탐색 못하는 경우
            left = mid + 1 
    return answer
