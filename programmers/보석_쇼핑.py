def solution(gems):
    answer = []
    left = 0
    cnt = len(set(gems))
    right = 0
    dic = {}
    # end를 0부터 늘리면서 start를 최대한으로 크게 를 반복!
    while right < len(gems):
        gem = gems[right]
        if gem in dic:
            dic[gem] += 1
        else:
            dic[gem] = 1
        while left < right:
            gem = gems[left]
            if gem in dic and dic[gem] > 1:
                dic[gem] -= 1
                left += 1
            else:
                break
        if len(dic) == cnt:
            answer += [(left + 1, right + 1)]
        right += 1
    return sorted(answer, key = lambda x: x[1] - x[0])[0]
