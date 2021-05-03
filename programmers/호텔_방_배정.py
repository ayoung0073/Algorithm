import sys
sys.setrecursionlimit(10**9) # 효율성 테스트 4 통과

def rfind(visited, idx):
    if idx not in visited: 
        visited[idx] = idx + 1
        return idx
    else:
        ret = rfind(visited, visited[idx]) # visited[idx] > 0 인 상태
        visited[idx] = ret + 1
        return ret
    
def solution(k, room_number):
    answer = []
    visited = dict() # [] -> {} 효율성 테스트 5, 6, 7 통과됨
    for num in room_number:
        idx = rfind(visited, num)
        answer.append(idx)
    return answer
