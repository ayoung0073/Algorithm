def solution(n):
    answer = ''
    q = n // 3
    r = n % 3
    while True:
        if r == 0: 
            answer = '4' + answer
            q -= 1
        elif r == 1: answer = '1' + answer
        elif r == 2: answer = '2' + answer
        
        if q <= 0: 
            return answer
        
        r = q % 3
        q = q // 3
      
    return answer

'''
3을 나눈 나머지가 0->4, 1->1, 2->2
몫을 또 3을 나눈 나머지가 그 앞자리 (몫이 0일 때까지 반복)
나머지가 0이면 (몫 - 1)로 3을 나눔
'''

# 함께 보면 좋을 코드!
'''
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
'''
