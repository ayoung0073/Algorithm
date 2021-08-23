## 14502. 연구소 

from itertools import combinations
from collections import deque
import sys
import copy

input = sys.stdin.readline 
n, m = map(int, input().split())
zero = []
virus = []

arr = [[0] * m for _ in range(n)]

for row in range(n):
    arr[row] = list(map(int, input().split()))
    for col in range(m):
      if arr[row][col] == 0:
        zero.append((row, col))
      elif arr[row][col] == 2:
        virus.append((row, col))

move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
def bfs(arr):
  q = deque(virus)
  while q:
    now = q.popleft()
    for dx, dy in move:
      next_x = now[0] + dx
      next_y = now[1] + dy
      if 0 <= next_x < n and 0 <= next_y < m:
        if arr[next_x][next_y] == 0:
          arr[next_x][next_y] = 2
          q.append((next_x, next_y))

  ret = 0
  for row in arr:
    ret += row.count(0)
  return ret

ans = 0
for walls in combinations(zero, 3):
  now = copy.deepcopy(arr)
  for wall in walls:
    # 세 개 벽 추가
    now[wall[0]][wall[1]] = 1
  
  ans = max(bfs(now), ans)

print(ans)
