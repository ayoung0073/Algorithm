from itertools import permutations

def solution(expression):
    answer = 0
    
    save_cal = []
    for i in expression:
        if i == '+':
            save_cal.append('+')
        elif i == '-':
            save_cal.append('-')
        elif i == '*':
            save_cal.append('*')
            
    string = expression.replace('+', ' ').replace('-', ' ').replace('*', ' ')
    save_val = string.split()
    
    prior_list = list(permutations(['+', '-', '*'], 3))

    for prior in prior_list:
        cal = save_cal[:] # == save_cal + []
        val = save_val[:]
        for i in prior:
            while i in cal:
                idx = cal.index(i)
                del cal [idx] 
                
                val_1 = val[idx]
                val_2 = val[idx + 1]
                del val[idx:idx + 2] 
                
                eval(val_1 + i + val_2)
                val.insert(idx, str(eval(val_1 + i + val_2)))
                
        answer = max(answer, abs(int(val[0])))
    return answer

'''
100 200 300 500 20
- * - +

첫번째 +(3) : 500 + 20 = 520 > 500, 20(index 3, 4) 제거 > index 3에 520 추가(arr.insert(3, 520)

100 200 300 520

두번째 -(0) : 100 - 200 = -100 > 100, 200(index 0, 1) 제거 > arr.insert(0, -100)

(연산자도 pop해야할 듯 하다..)

-100 300 520

세번째 -(1) : 300 - 520 = -220

'''
