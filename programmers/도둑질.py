def solution(money):
    n = len(money)
    
    dp = [0] * n # 첫집을 터는 경우
    dp[0] = money[0]
    dp[1] = money[0]
    
    for i in range(2, n - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
        
    dp_last = [0] * n # 마지막 집을 터는 경우
    dp_last[n - 1] = money[n - 1]
    dp_last[n - 2] = money[n - 1]
    
    for i in range(n - 3, 0, -1):
        dp_last[i] = max(dp_last[i + 1], dp_last[i + 2] + money[i])
        
    return max(dp[n - 2], dp_last[1])
