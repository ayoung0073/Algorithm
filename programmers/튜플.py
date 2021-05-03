def solution(s):
    answer = []
    s = s.replace('{{','').replace('}}','').split('},{')
    arr = []
    
    for i in s:
        arr.append(list(map(int, i.split(','))))
        
    arr.sort(key = len) # 길이에 따라 정렬 arr.sort(key = lambda x : len(x))
    
    for i in arr:
        for j in i:
            if not j in answer:
                answer.append(j)
                break
    return answer
