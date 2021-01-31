def check(answer):
    for x, y, a in answer:
        if a == 0: # 기둥 설치한 경우
            if y == 0 or ([x - 1, y, 1] in answer) or ([x, y, 1] in answer) or ([x, y - 1, 0] in answer): # 기둥 설치 조건
                continue
            return False # 조건 벗어나면 False 반환
        if a == 1: 
            if ([x, y - 1, 0] in answer) or ([x + 1, y - 1, 0] in answer) or ([x - 1, y, 1] in answer and ([x + 1, y, 1] in answer)): # 보 설치 조건
                continue
            return False
    return True            

def solution(n, build_frame):
    answer = []
    
    for build in build_frame:
        x, y, a, b = build # x, y : 교차점 좌표, a : 기둥(0), 보(1), b : 삭제(0), 설치(1)
        if a == 0: # 기둥인 경우
            if b == 1: # 설치
                answer.append([x, y, 0])
                if not check(answer):
                    answer.remove([x, y, 0])
            else: # 삭제
                answer.remove([x, y, 0])
                if not check(answer):
                    answer.append([x, y, 0])
                    
        elif a == 1: # 보인 경우
            if b == 1: # 설치
                answer.append([x, y, 1])
                if not check(answer):
                    answer.remove([x, y, 1])
            else: # 삭제
                answer.remove([x, y, 1])
                if not check(answer):
                    answer.append([x, y, 1])
        
    answer = sorted(answer, key = lambda x : (x[0], x[1], x[2]))
    return answer
