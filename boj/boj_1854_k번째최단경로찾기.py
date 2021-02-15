## 1854. K번째 최단 경로 찾기
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, k = map(int, input().split())

info = [[] for _ in range(n)]
distance = [[INF for _ in range(k)] for _ in range(n)]

for _ in range(m):
  a, b, c = map(int, input().split())
  info[a - 1].append((c, b - 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    for i in info[now]:
      a, b = i
      cost = dist + a
      if distance[b][k - 1] > cost:
        distance[b][k - 1] = cost
        distance[b].sort()
        heapq.heappush(q, (cost, b))

distance[0][0] = 0
dijkstra(0)
      
for i in distance:
  if i[k - 1] == INF:
    print(-1)
  else:
    print(i[k - 1])
