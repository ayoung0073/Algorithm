def solution(record):
    answer = []
    dic = dict() # 아이디, 닉네임 매핑
    arr = []
    for i in record:
        action = i.split()
        if action[0] == 'Enter':
            dic[action[1]] = action[2]
            arr.append((action[1], 0))
        if action[0] == 'Leave':
            arr.append((action[1], 1))
        if action[0] == 'Change':
            dic[action[1]] = action[2]
            
    for i in arr:
        if i[1] == 0: 
            answer.append(dic[i[0]] + "님이 들어왔습니다.")
        else:
            answer.append(dic[i[0]] + "님이 나갔습니다.")
    return answer
