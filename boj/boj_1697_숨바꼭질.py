from collections import deque
n, k = map(int, input().split())
q = deque([(n, 0)])
INF = 100001
visited = [False] * INF
sec = 0
while q:
  x, sec = q.popleft()
  visited[x] = True

  if x == k: break
  if x - 1 >= 0 and not visited[x - 1]:
    q.append((x - 1, sec + 1))
  if x + 1 < INF and not visited[x + 1]:
    q.append((x + 1, sec + 1))
  if 2 * x < INF and not visited[2 * x]:
    q.append((x * 2, sec + 1))

print(sec)
