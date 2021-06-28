## 1495. 기타리스트

import sys  
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [[False for _ in range(m + 1)] for _ in range(n)]
# dp[index][volume]
if s + v[0] <= m:
  dp[0][s + v[0]] = True
if s - v[0] >= 0:
  dp[0][s - v[0]] = True

for i in range(n - 1):
  for j in range(m + 1):
    if dp[i][j]: # 
      if j + v[i + 1] <= m:
        dp[i + 1][j + v[i + 1]] = True
      if j - v[i + 1] >= 0:
        dp[i + 1][j - v[i + 1]] = True

for vol in range(m, -1, -1):
  if dp[n - 1][vol]:
    print(vol)
    exit(0)
    
print(-1)
