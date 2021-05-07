## 최소 비용 구하기
import sys
import heapq

input = sys.stdin.readline

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  s, e, cost = map(int, input().split())
  graph[s].append((cost, e)) # 출발지 s에서 e까지의 비용

INF = int(1e9)
distance = [INF] * (n + 1)
start, end = map(int, input().split())

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    cost, now = heapq.heappop(q)
    if distance[now] < cost:
      continue
    for i in graph[now]:
      if distance[i[1]] > i[0] + cost: # 갱신 조건
        distance[i[1]] = i[0] + cost
        heapq.heappush(q, (distance[i[1]], i[1]))

dijkstra(start)
print(distance[end])
