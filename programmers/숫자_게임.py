# 1 deque, while문 이용
from collections import deque
def solution(A, B):
    answer = 0
    A.sort() 
    B.sort()
    
    q = deque(B)

    a_idx = 0
    b_idx = 0
    
    while q:   
        if b_idx == len(A):
            break
            
        if A[a_idx] < q[0]:
            q.popleft()
            a_idx += 1
            answer += 1
            continue
            
        b_idx += 1
        q.append(q.popleft())
    
    return answer

# 2 배열 인덱스 이용
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    j = 0
    
    for i in range(len(B)):
        if A[j] < B[i]:
            answer += 1
            j += 1

    return answer
