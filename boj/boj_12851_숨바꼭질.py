## 12851. 숨바꼭질2

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

q = deque()

q.append((0, n))
ans = int(1e9)
ans_cnt = 0
dp = [int(1e9)] * 100001
while q:
  cnt, now = q.popleft()

  if now == k:
    if ans == int(1e9):
      ans = cnt
      ans_cnt += 1
    elif cnt == ans:
      ans_cnt += 1
    continue

  if cnt > ans:
    break

  else:
    if now - 1 >= 0 and cnt + 1 <= dp[now - 1]:
      q.append((cnt + 1, now - 1))
      dp[now - 1] = cnt + 1
    if now + 1 <= 100000 and cnt + 1 <= dp[now + 1]:
      q.append((cnt + 1, now + 1))
      dp[now + 1] = cnt + 1
    if now * 2 <= 100000 and cnt + 1 <= dp[now * 2]:
      q.append((cnt + 1, now * 2))
      dp[now * 2] = cnt + 1

print(ans)
print(ans_cnt)
