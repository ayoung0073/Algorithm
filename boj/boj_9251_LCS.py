a = input()
b = input()

len1 = len(a)
len2 = len(b)

dp = [[0 for _ in range(len2 + 1)] for _ in range(len1 + 1)]

for i in range(1, len1 + 1):
  for j in range(1, len2 + 1):
    if a[i - 1] == b[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[-1][-1])
