## 12865. 평범한 배낭

n, k = map(int, input().split())
bags = []
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(n):
  w, v = map(int, input().split())
  bags.append((w, v))

for i in range(1, n + 1): # i : bag
  for j in range(1, k + 1): # j : 무게
    if bags[i - 1][0] <= j:
      dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - bags[i - 1][0]] + bags[i - 1][1])
    else:
      dp[i][j] = dp[i - 1][j]

print(dp[n][k])
