def solution(N, number):
    dp = [0, [N]] 
    if N == number:  
        return 1
    for i in range(2, 9): # 횟수 2 ~ 8
        case = [] # 임시 케이스 셋
        basic_num = int(str(N) * i) # 같은 숫자 반복
        case.append(basic_num)
        for i_half in range(1, i // 2 + 1): 
            for x in dp[i_half]:
                for y in dp[i - i_half]: # x와 y를 더하면 i가 되도록 만드는 수
                    case.append(x + y)
                    case.append(x - y)
                    case.append(y - x)
                    case.append(x * y)
                    if y != 0:
                        case.append(x / y)
                    if x != 0:
                        case.append(y / x)
            if number in case:
                return i
            dp.append(case) 
    return -1 
