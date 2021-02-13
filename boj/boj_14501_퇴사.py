## 1. DP 2차원 배열
import sys
input = sys.stdin.readline

n = int(input())

dp = [[0 for j in range(n)] for i in range(n + 1)] # 다이나믹 프로그래밍
result = [0] * (n + 1)

for i in range(n):
  a, b = map(int, input().split())
  if i + a <= n: # 일 수를 포함해 n일을 넘지 않는 조건에만 
    result[i] = b
    for j in range(i, i + a):
      dp[i][j] = b

  idx = n # 이 코드 없으면 index error
  check = False
  for j in range(i):
    if dp[j][i] == 0: # 합칠 수 있는 조건
      check = True
      if result[j] > result[idx]: # 최댓값을 해당 dp 배열에 합친다.
        idx = j

  if check: # 합칠 수 있을 때 
    result[i] += result[idx]
    for k in range(i):
      dp[i][k] = dp[idx][k]  

print(max(result))

## 2. DP 1차원 배열 역순으로 계산
import sys
input = sys.stdin.readline

n = int(input())
table = []
for i in range(n):
  a, b = map(int, input().split())
  table.append((a, b))

dp = [0] * (n + 1) # 다이나믹 프로그래밍

for i in range(n - 1, -1, -1):
  if table[i][0] + i <= n: # 일수가 넘어가지 않을 때 
    dp[i] = max(table[i][1] + dp[i + table[i][0]], dp[i + 1])
  else:
    dp[i] = dp[i + 1]

print(dp[0])
