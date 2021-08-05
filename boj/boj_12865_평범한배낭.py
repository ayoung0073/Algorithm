## 12865. 평범한 배낭

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
weights = [0] * (n + 1)
values = [0] * (n + 1)

for i in range(1, n + 1):
  weights[i], values[i] = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  for j in range(1, k + 1):
    if j < weights[i]:
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j - weights[i]] + values[i], dp[i - 1][j])

print(dp[n][k])


## 재귀
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int, input().split())))

dp = [[0] * (k + 1) for _ in range(n)]

def pack(idx, w):

  if idx == n:
    return 0
  if w >= k:
    return 0
  if dp[idx][w] == 0:
    
    v1 = 0
    if w + arr[idx][0] <= k: # 현재 물건을 포함할 때 버틸 수 있으면 v1 갱신
      v1 = arr[idx][1] + pack(idx + 1, w + arr[idx][0])
    v2 = pack(idx + 1, w) # 현재 물건을 포함하지 않은 경우

    max_value = max(v1, v2)
    dp[idx][w] = max_value

  return dp[idx][w]
print(pack(0, 0))
