def solution(priorities, location):
    answer = 0
    
    while True:
        max_priority = max(priorities)
        priority = priorities.pop(0)
        
        if priority < max_priority:
            priorities.append(priority)
        else:
            answer += 1
            if location == 0:
                return answer
            
        location = (location - 1) % len(priorities)
