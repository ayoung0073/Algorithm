n = int(input())

dp = [i for i in range(101)]

for i in range(4, n + 1):
  # dp[i - 3] (i - 3)에서 전체선택, 복사, 붙여넣기 : dp[i - 3] * 2
  # dp[i - 4] 전체선택, 복사, 붙여넣기, 붙여넣기 : dp[i - 4] * 3
  # ...

  for j in range(i - 1, 0, -1):
    dp[i] = max(dp[i - j] * (j - 1), dp[i])

print(dp[n])
