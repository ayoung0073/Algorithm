## 14238. 출근 기록
import sys

s = input()

obj = [s.count(word) for word in ('A', 'B', 'C')] # A, B, C 개수 카운트
# dp[a 개수][b 개수][c 개수][전전날][전날]
dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(len(s))] for _ in range(len(s))] for _ in range(len(s))]

answer = [''] * len(s)

def dfs(a, b, c, prev):
  if [a, b, c] == obj:
    print(''.join(answer))
    sys.exit()

  if dp[a][b][c][prev[0]][prev[1]]:
    return False

  dp[a][b][c][prev[0]][prev[1]] = True
  
  if a + 1 <= obj[0]:
    answer[a + b + c] = 'A'
    if dfs(a + 1, b, c, [prev[1], 0]):
      return True

  if b + 1 <= obj[1]:
    answer[a + b + c] = 'B'
    if prev[1] != 1:
      if dfs(a, b + 1, c, [prev[1], 1]):
        return True

  if c + 1 <= obj[2]:
    answer[a + b + c] = 'C'
    if prev[0] != 2 and prev[1] != 2:
      if dfs(a, b, c + 1, [prev[1], 2]):
        return True

  return False

dfs(0, 0, 0, [0, 0])
print(-1)
