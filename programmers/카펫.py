def solution(brown, yellow):
    # 전체 격자의 수 : brown + yellow 
    all = brown + yellow
    # yellow를 기준으로 행을 추가
    for i in range(1, yellow + 1):
        if (yellow % i) != 0:
            continue
        # 열 길이
        col_length = yellow // i + 2
        if all % col_length == 0: # [전체 격자 % 열 길이] 나누어 떨어지는 경우 답
            return [col_length, i + 2]
        
    return [0, 0]
