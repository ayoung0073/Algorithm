def solution(s): # 입력받은 문자열 s
    # before
    result = length = len(s)
    cnt = 0
    before = ''
    for i in range(1, length // 2 + 1):
        arr = [s[j:j+i] for j in range(0, length, i)] # i의 길이단위로 문자열 자르기
        string = '' # i의 길이 단위로 잘라 압축했을 때의 결과값 저장
        before = '' # 이전 문자열 저장
        cnt = 0 # 동일 문자열 세는 변수 0으로 초기화
        for k in arr:
            if before == k: # 이전 문자열과 동일한 경우
                cnt += 1
            else: # 동일하지 않을 경우 경우 3가지로 나뉨
                if cnt == 0: # 가장 처음 요소인 경우는 cnt = 0
                    cnt += 1 
                    pass
                elif cnt == 1: # before 문자열이 한번 나타난 경우는 1제외하고 문자열만 append
                    string += before
                else:
                    string += str(cnt) + before 
                    cnt = 1
                    
                before = k
                
        # 요소 남은 경우
        if cnt != 1: 
            string += str(cnt) + before
        else:
            string += before
        
        result = min(result, len(string)) # 반복할 때마다 짧은 길이 갱신
        
    return result

# 문자열 일정 길이로 자르기
# map(''.join, zip(*[iter(seq)]*length))
# [seq[i:i+length] for i in range(0, len(seq), length)]
        
