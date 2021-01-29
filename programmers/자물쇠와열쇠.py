# key의 회전 함수(시계방향)
def rotate90(mat):
    length = len(mat)
    ret = [[0] * length for _ in range(length)]

    for r in range(length):
        for c in range(length):
            ret[c][length - 1 - r] = mat[r][c]
            
    return ret

# key의 행렬과 lock의 행렬 체크 함수
def check(lock, n, m): # lock, len(lock), len(key)
    for i in range(n): # lock 길이만큼 반복
        for j in range(n):
            if lock[n + i][n + j] != 1: # 해당 범위내에 있는 값이 1이 아니면 False
                return False
    return True
    
def solution(key, lock):
    # lock의 0부분을 key의 1로 채우기
    # lock의 1과 key의 1이 만나면 안됨
    n, m = len(lock), len(key)
    
    # lock(자물쇠)의 크기를 3배 확장
    new_lock = [[0] * (n * 3) for _ in range(n * 3)] # [n * 3][n * 3]
    
    # 중앙에 기존 자물쇠 대입
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
            
    for _ in range(4): # 4방향 확인
        key = rotate90(key) # key 회전
        
        for x in range(2 * n):
            for y in range(2 * n):
                
                # 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                        
                if check(new_lock, n, m): # 자물쇠로 열 수 있는 경우 True 반환
                    return True
            
                # 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
                        
    return False
