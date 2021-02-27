## 14226. 이모티콘
from collections import deque
n = int(input())
INF = int(1e9)
dp = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
# 행 : 화면에 있는 이모티콘 개수
# 열 : 클립보드에 있는 이모티콘 개수
# value : 초
dp[1][0] = 0
q = deque([(1, 0)])

while q:
  num, copy = q.popleft()
  sec = dp[num][copy]
  # 전체를 복사하는 경우
  if num <= n:
    if dp[num][num] == INF:
      dp[num][num] = sec + 1
      q.append((num, num))
  # 붙여넣기 하는 경우
  if num + copy <= n:
    if dp[num + copy][copy] == INF:
      dp[num + copy][copy] = sec + 1
      q.append((num + copy, copy))
  # 하나의 이모티콘 삭제하는 경우
  if num >= 1:
    if dp[num - 1][copy] == INF:
      dp[num - 1][copy] = sec + 1
      q.append((num - 1, copy))
  if num == n: # 화면에 보이는 이모티콘이 n인 경우
    break

print(min(dp[n]))
