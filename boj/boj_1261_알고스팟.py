# deque 이용하자
from collections import deque

# 가로 n, 세로 m
n, m = map(int, input().split())
maze = []

def check_range(x, y):
  if x < 0 or y < 0 or x >= m or y >= n:
    return False
  return True

for i in range(m):
  maze.append(list(map(int, input())))

counts = [[-1 for j in range(n)] for i in range(m)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()


result = 0
q.append((0, 0))
counts[0][0] = 0
while q:
  x, y= q.popleft()
  #print(x, y)
 # if cost == 1: result += 1 
  for i in range(4):
    if check_range(x + dx[i], y + dy[i]):
      if counts[x + dx[i]][y + dy[i]] == -1:
        if maze[x + dx[i]][y + dy[i]] == 0:
          q.appendleft((x + dx[i], y + dy[i]))
          counts[x + dx[i]][y + dy[i]] = counts[x][y]
        else:
          q.append((x + dx[i], y + dy[i]))
          counts[x + dx[i]][y + dy[i]] = counts[x][y] + 1

print(counts[m - 1][n - 1])
