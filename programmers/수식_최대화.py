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
        cal = save_cal + []
        val = save_val + []
        for i in prior:
            while i in cal:
                idx = cal.index(i)
                print(idx)
                del cal [idx] 
                print(val)
                val_1 = int(val[idx])
                val_2 = int(val[idx + 1])
                del val[idx:idx + 2] 
                if i == '+':
                    val.insert(idx, val_1 + val_2)
                elif i == '-':
                    val.insert(idx, val_1 - val_2)
                elif i == '*':
                    val.insert(idx, val_1 * val_2)
                    
        answer = max(answer, abs(val[0]))
    return answer
