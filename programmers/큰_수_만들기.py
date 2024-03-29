def solution(number, k):
    answer = []
    
    length = len(number)
    k = length - k
    start_idx = 0
    
    while k != 0:
        end_idx = length - k
        max_idx = start_idx
        
        for i in range(start_idx + 1, end_idx + 1):
            if number[max_idx] < number[i]:
                max_idx = i
            if number[i] == '9': # 테스트 10 통과 기준
                break  
                
        start_idx = max_idx + 1
        k -= 1
        answer.append(number[max_idx]) 
        
    return ''.join(str(i) for i in answer)


### 2
def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    return ''.join(stack[:len(stack) - k])
