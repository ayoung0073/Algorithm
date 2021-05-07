def solution(distance, rocks, n):
    answer = 0
    left = 0
    right = distance
    rocks.sort()
    gap = 0
    while left <= right:
        cnt = 0
        now = 0
        mid = (left + right) // 2
        
        arr = [0]
        for i in range(0, len(rocks)):
            if rocks[i] < mid + now: # remove 조건
                cnt += 1
                if cnt > n:
                    break
            else:
                now = rocks[i]
                arr.append(rocks[i])
                
        if cnt <= n:
            arr.append(distance)
            gap = int(1e9)
            for i in range(0, len(arr) - 1):
                gap = min(gap, arr[i + 1] - arr[i])
            answer = max(gap, answer)
            left = mid + 1
            
        else:
            right = mid - 1
        
    return answer
