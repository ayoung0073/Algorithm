answer = []
def solution(user_id, banned_id):
    global answer
    user_len = len(user_id)
    banned_len = len(banned_id) # 만약 dfs에서 추가된 arr 길이가 banned_len과 같으면 answer 추가
    check_list = [[-1 for _ in range(user_len)] for _ in range(banned_len)] # 매칭되는지 체크하는 배열
    
    def dfs(banned_idx, arr):
        global answer
        # banned_id[banned_idx]와 겹치는 게 있는지 비교
        # 그 중, arr에 있으면 pass
        # 없다면 arr에 추가한 후, dfs 재귀 호출
        for i in range(user_len):
            if check_list[banned_idx][i] == -1: # 갱신해야하는 경우, 선처리
                check = True
                # 길이부터 체크하자
                if len(user_id[i]) != len(banned_id[banned_idx]): # 틀린 경우
                    check_list[banned_idx][i] = 0
                    continue
                else:
                    # 문자 모두 비교
                    for j in range(len(user_id[i])):
                        if user_id[i][j] != banned_id[banned_idx][j] and banned_id[banned_idx][j] != '*':
                            check = False
                            break
                    if check:
                        check_list[banned_idx][i] = 1 # 맞는 경우 1로 갱신
                    else:
                        check_list[banned_idx][i] = 0 # 틀린 경우 0으로 갱신

        
            if check_list[banned_idx][i] == 1:
                # 이제 겹치는 거 있는지 확인
                if user_id[i] not in arr:
                    if len(arr) + 1 == banned_len and set(arr + [user_id[i]]) not in answer: # (1) 집합 이용
                        answer.append(set(arr + [user_id[i]]))
                        continue
#                     if len(arr) + 1 == banned_len: # (2)
#                         answer.append(sorted(arr + [user_id[i]])) # 정렬해야한다 그래야 set() 비교 가능(정렬된 리스트이용) 첫번째 생각해냄
#                         continue
                    if banned_idx + 1 < banned_len:
                        dfs(banned_idx + 1, arr + [user_id[i]])
        
    arr = []
    dfs(0, arr)
    
    # sorted된 각 배열 중, 같은 배열 중복 제거
#    ret = list(set([tuple(set(item)) for item in answer])) (2)
    
    return len(answer) # (1)
#     return len(ret) # (2)
