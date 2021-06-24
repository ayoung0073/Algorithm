from itertools import combinations
import operator

def solution(orders, course):
    answer = []
    courses = {}
    for order in orders:
        for num in course:
            arr = list(combinations(order, num)) # 각 코스 개수마다 combination 진행
            for a in arr:
                a = sorted(list(a)) # 오름차순 정렬하여 문자열로 만들기 
                i = ''.join(a)
                if i in courses:
                    courses[i] += 1
                else:
                    courses[i] = 1

    courses = dict(sorted(courses.items(), key=operator.itemgetter(1), reverse=True)) # value를 기준으로 정렬하여 딕셔너리로 만들기
    check = {} # result에 담을 수 있는지 check
    for c in courses:
        if courses[c] >= 2 and (len(c) not in check or check[len(c)] <= courses[c]):
            check[len(c)] = courses[c] 
            answer.append(c)
                    
    return sorted(answer)
