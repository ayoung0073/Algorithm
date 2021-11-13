def solution(d, budget):
    answer = 0
    d.sort()
    for now in d:
        budget -= now
        if budget < 0: 
            break
        answer += 1
    return answer
