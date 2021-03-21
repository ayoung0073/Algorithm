## 1495. 기타리스트

import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
gap = [s] + list(map(int, input().split()))

# [곡번호][볼륨크기]
dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

def check_range(vol):
  if vol < 0 or vol > m:
    return False
  return True

if check_range(s - gap[1]):
  dp[1][s - gap[1]] = True
if check_range(s + gap[1]):
  dp[1][s + gap[1]] = True

for i in range(1, n):
  for j in range(m + 1):
    if dp[i][j]:
      if check_range(j + gap[i + 1]):
        dp[i + 1][j + gap[i + 1]] = True
      if check_range(j - gap[i + 1]):
        dp[i + 1][j - gap[i + 1]] = True

check = False
for i in range(m, -1, -1): # 범위 조심.. (m, 0, -1) 함
  if dp[n][i]:
    print(i)
    check = True
    break

if not check:
  print(-1)

