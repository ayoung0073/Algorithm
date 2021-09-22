answer = 0
def solution(numbers, target):
    def dfs(idx, now): # 현재 인덱스, 현재 값
        global answer 
        if idx == len(numbers) - 1: # 마지막 인덱스인 경우 재귀 함수 종료
            if now == target:
                answer += 1
            return
        dfs(idx + 1, now + numbers[idx + 1])
        dfs(idx + 1, now + (-1) * numbers[idx + 1])
        
    dfs(-1, 0)
    
    return answer
