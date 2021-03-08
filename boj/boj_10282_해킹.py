import sys
import heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, d, c = map(int, input().split())
  cnt = 0
  graph = [[] for _ in range(n + 1)]
  visited = [False for _ in range(n + 1)]
  for _ in range(d): # 의존성
    a, b, s = map(int, input().split())
    graph[b].append((a, s))
  
  q = [(0, c)]
  # heapq.heappush(q, (0, c))
  # visited[c] = True
  res = 0
  # cnt += 1
  while q:
    sec, now = heapq.heappop(q)
    if not visited[now]:
      cnt += 1
      visited[now] = True
      res = sec
      for i in graph[now]:
        if not visited[i[0]]:
          heapq.heappush(q, (sec + i[1], i[0]))

  print(cnt, res)
