def check(stones, num, k):
    cnt = 0
    for i in range(len(stones)):
        if stones[i] <= num:
            cnt += 1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True
    
        
def solution(stones, k):
    answer = 0
    left = 0
    right = 200000000

    while left <= right:
        mid = (left + right) // 2 # 학생 수
        if check(stones, mid, k):
            left = mid + 1
        else:
            right = mid - 1
        
    return left
