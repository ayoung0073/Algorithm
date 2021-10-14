from collections import defaultdict

def solution(clothes):
    clothes_count = defaultdict(int)
    
    for c in clothes:
        clothes_count[c[1]] += 1
    
    answer = 1
    for clothes in clothes_count:
        answer *= (clothes_count[clothes] + 1)
    
    return answer - 1 # 최소 한 개의 의상은 입어야 한다.
