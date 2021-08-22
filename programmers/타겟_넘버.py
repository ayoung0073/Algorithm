from collections import deque
def solution(numbers, target):
    q = deque()
    
    q.append(numbers[0])
    q.append((-1) * numbers[0])
    
    for i in numbers[1:]:
        length = len(q)
        for _ in range(length):
            num = q.popleft()
            q.append(num + i)
            q.append(num + (-1) * i)
    
    return q.count(target)
  
# 테스트 1 〉	통과 (205.46ms, 34.9MB)
# 테스트 2 〉	통과 (206.79ms, 34.6MB)
# 테스트 3 〉	통과 (0.20ms, 10MB)
# 테스트 4 〉	통과 (0.78ms, 10.3MB)
# 테스트 5 〉	통과 (6.37ms, 10.5MB)
# 테스트 6 〉	통과 (0.41ms, 10.1MB)
# 테스트 7 〉	통과 (0.28ms, 10.2MB)
# 테스트 8 〉	통과 (1.60ms, 10.3MB)
  
### DFS
answer = 0
def solution(numbers, target):
    last = len(numbers) - 1
    def dfs(index, num): # numbers의 index, 현재값
        global answer
        if index == last: # 마지막 index인 경우
            if num == target:
                answer += 1
                return
        else:
            dfs(index + 1, num + numbers[index + 1])
            dfs(index + 1, num + (-1) * numbers[index + 1])
        
    dfs(-1, 0)
    return answer
  
# 테스트 1 〉	통과 (323.17ms, 10MB)
# 테스트 2 〉	통과 (329.02ms, 10MB)
# 테스트 3 〉	통과 (0.32ms, 10.2MB)
# 테스트 4 〉	통과 (1.24ms, 10.1MB)
# 테스트 5 〉	통과 (10.14ms, 10.3MB)
# 테스트 6 〉	통과 (0.64ms, 10.1MB)
# 테스트 7 〉	통과 (0.33ms, 9.99MB)
# 테스트 8 〉	통과 (2.72ms, 10.2MB)
