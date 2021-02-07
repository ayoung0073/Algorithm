from collections import deque
import sys

input = sys.stdin.readline
n, l, r = map(int, input().split())

country = []
for _ in range(n):
  country.append(list(map(int, input().split())))

dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]

def check_range(x, y):
  if x < 0 or y < 0 or x >= n or y >= n:
    return False
  return True

def transfer(x, y, check):
  num_sum = country[x][y]
  count = 1
  united = [(x, y)]
  q = deque([(x, y)])
  check[x][y] = True
  while q:
    a, b = q.popleft()
    num = country[a][b]
    for k in range(4):
      if check_range(a + dx[k], b + dy[k]) and not check[a + dx[k]][b + dy[k]]:
        dist = abs(country[a + dx[k]][b + dy[k]] - num)
        if dist >= l and dist <= r:
          q.append((a + dx[k], b + dy[k]))
          check[a + dx[k]][b + dy[k]] = True
          count += 1
          num_sum += country[a + dx[k]][b + dy[k]]
          united.append((a + dx[k], b + dy[k]))


  add = num_sum // count

  for m, n in united:
    country[m][n] = add

  if count == 1: 
    return 0
  return 1

result = 0
index = 0

while True:
  check = [[False for _ in range(n)] for _ in range(n)]
  transfer_check = 0
  for i in range(n):
    for j in range(n): # 2차원 배열 탐색
      if not check[i][j]: # 아직 탐색하지 못한 위치인 경우
        transfer_check += transfer(i, j, check)

  if transfer_check == 0:
    break
  result += 1

print(result)
