n = int(input())
power = list(map(int, input().split()))
power.reverse() # LIS 알고리즘을 위해 역순

dp = [1] * n

for i in range(1, n):
  for j in range(i):
    if power[j] < power[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
