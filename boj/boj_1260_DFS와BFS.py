from collections import deque

n, m, start = map(int, input().split())
mat = [[0]*n for _ in range(n)]

for k in range(m):
  i, j = map(int, input().split())
  mat[i - 1][j - 1] = 1
  mat[j - 1][i - 1] = 1

visited = [False] * n

def dfs(mat, v, visited):
  visited[v] = True
  print(v+1, end = ' ')
  for i in range(len(mat[v])):
    if visited[i] != True and mat[v][i] == 1:
      dfs(mat, i, visited)

def bfs(mat, v, visited):
  queue = deque([v])
  visited[v] = True
  while queue:
    v = queue.popleft()
    print(v + 1, end = ' ')
    for i in range(len(mat[v])):
      if visited[i] != True and mat[v][i] == 1:
        visited[i] = True
        queue.append(i)

dfs(mat, start - 1, visited)
visited = [False] * n
print()
bfs(mat, start - 1, visited)
