# 정렬 이용
def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        
    return participant[len(participant) - 1]

# dictionary 이용
def solution(participant, completion):
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for i in completion:
        dic[i] -= 1

    for i in participant:
        if dic[i] == 1:
            return i
