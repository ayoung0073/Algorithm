def solution(enroll, referral, seller, amount):
    answer = []
    dic = dict(zip(enroll, referral))
    res = dict(zip(enroll, [0] * len(enroll)))
    res['-'] = 0
    
    for i in range(len(seller)):
        employee = seller[i]
        money = amount[i] * 100
        res[employee] += money
        
        while True:
            if employee == '-':
                break
            profit = money // 10
            
            res[employee] -= profit
            res[dic[employee]] += profit
            
            employee = dic[employee]
            money = profit

    return list(res.values())[0:-1]
