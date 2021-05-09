import math
def solution(n, stations, w):
    answer = 0
    
    distance = [] # 전파 닿지 않는 거리 계산 (0이하 : 전파 닿음)
    for i in range(1, len(stations)):
        distance.append((stations[i] - w) - (stations[i - 1] + w + 1))
        
    distance.append(stations[0] - w - 1)
    distance.append(n - stations[-1] - w)
    
    for i in distance:
        if i <= 0: continue
        answer += math.ceil(i / ((w*2) + 1))

    return answer
