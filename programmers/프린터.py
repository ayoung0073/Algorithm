# 1 del 이용
def solution(priorities, location):
    answer = 0
    idx = location
    n = len(priorities)
    
    while True:
        
        first = priorities[0]
        
        if idx == 0 and max(priorities) == first:
            answer += 1
            break
            
        if max(priorities) == first:
            del priorities[0]
            answer += 1
            n -= 1
            
        else:
            del priorities[0]
            priorities.append(first)
            
        idx = (idx - 1) % n
    return answer
  
 # 2 pop 이용 
  def solution(priorities, location):
    answer = 0
    idx = location
    n = len(priorities)
    
    while n:
        max_value = max(priorities)
        first = priorities.pop(0)  
        n -= 1
        
        if idx == 0:
            idx = n
        else:
            idx = (idx - 1) % n
        
        if idx == n and max_value == first:
            answer += 1
            break
            
        if max_value == first:
            answer += 1
            
        else:
            priorities.append(first)
            n += 1
            
    return answer
