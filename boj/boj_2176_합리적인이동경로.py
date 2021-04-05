## 2176. 합리적인 이동 경로

import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

INF = sys.maxsize
visited = [INF] * (n + 1)
count = [0] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 2))

count[2] = 1
visited[2] = 0

while q:
  dist, now = heapq.heappop(q)
  if dist > visited[now]:
    continue

  for i in range(len(graph[now])):
    if visited[graph[now][i][0]] > dist + graph[now][i][1]:
      visited[graph[now][i][0]] = dist + graph[now][i][1]
      heapq.heappush(q, (visited[graph[now][i][0]], graph[now][i][0]))
      # q.append((graph[now][i][0], visited[graph[now][i][0]]))

    if visited[graph[now][i][0]] < dist:
      count[now] += count[graph[now][i][0]]
      
print(count[1])
