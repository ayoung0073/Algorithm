# 토마토

import sys 
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
dp = [] # 얼마나 걸리는지 저장하는 배열

q = deque()
for i in range(n):
  dp.append(list(map(int, input().split())))
  for j in range(m):
    if dp[i][j] == 1: # 익은 토마토 배열에 추가
      q.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
  i, j = q.popleft()
  for k in range(4):
    x, y = i + dx[k], j + dy[k]
    if 0 <= x < n and 0 <= y < m and dp[x][y] == 0:
      q.append((x, y))
      dp[x][y] = dp[i][j] + 1

ans = 0
for arr in dp:
  if 0 in arr:
    print(-1)
    exit(0)
  ans = max(max(arr), ans)

print(ans - 1)
# print(max(max(dp)) - 1) # 실패
