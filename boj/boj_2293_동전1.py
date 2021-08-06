import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k + 1)] # index: 가치, value: 경우의 수
dp[0] = 1 # 동전을 1개만 쓸 때 사용한다.
'''
예시를 살펴보자.
입력이 1, 2, 5일 때
dp[2] = dp[0] 일 것이다.
      = 1 !!
'''

# k원이 될 수 있는 경우의 수를 찾아라
for coin in coins:
  # i는 현재 추가하려는 가치(가격)이 될 것이다.
  for i in range(coin, k + 1): # coin을 포함한 이유 : 동전의 개수가 1개일 때를 생각해야 한다. (위의 예시)
    dp[i] += dp[i - coin]  # 경우의 수를 추가한다. 

print(dp[k])
