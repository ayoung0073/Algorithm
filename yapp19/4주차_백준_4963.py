## 4963 섬의 개수 

import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(100000)

dx = [-1, -1, -1, 1, 1, 1, 0, 0] # 왼 오
dy = [1, 0, -1, 1, 0, -1, 1, -1] # 아래 위

def dfs(maps, visited, i, j):
  for idx in range(8):
    x = i + dx[idx]
    y = j + dy[idx]
    if 0 <= x < len(maps) and 0 <= y < len(maps[0]) and not visited[x][y] and maps[x][y] != 0:
      visited[x][y] = True
      dfs(maps, visited, x, y)

while True:
  w, h = map(int, input().split())
  if (w, h) == (0, 0):
    sys.exit()
  visited = [[False] * w for _ in range(h)]
  maps = []
  for _ in range(h):
    maps.append(list(map(int, input().split())))
  answer = 0
  for i in range(h):
    for j in range(w):
      if not visited[i][j] and maps[i][j] != 0:
        dfs(maps, visited, i, j)
        answer += 1
  print(answer)

