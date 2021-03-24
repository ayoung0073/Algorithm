## 12101. 1, 2, 3 더하기 2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

cnt = 0

def dfs(num, arr):
  global cnt
  if num == n:
    cnt += 1
    if cnt == k:
      print('+'.join(str(i) for i in arr))
      sys.exit(0)
  if num + 1 <= n:
    tmp = arr + [1]
    dfs(num + 1, tmp)
  if num + 2 <= n:
    tmp = arr + [2]
    dfs(num + 2, tmp)
  if num + 3 <= n:
    tmp = arr + [3]
    dfs(num + 3, tmp)

dfs(0, [])
print(-1)
