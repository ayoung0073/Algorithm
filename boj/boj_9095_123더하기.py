import sys
input = sys.stdin.readline

t = int(input())
arr = []

for _ in range(t):
  arr.append(int(input()))

dp = [[0, 0, 0, 0] for _ in range(10001)]

dp[1][1] = 1

dp[2][1] = 1
dp[2][2] = 1

dp[3][1] = 2
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 10001):
  dp[i][1] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
  dp[i][2] = dp[i - 2][1] + dp[i - 2][2] + dp[i - 2][3]
  dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3]

for i in arr:
  print(sum(dp[i]))
