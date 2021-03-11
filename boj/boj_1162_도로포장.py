## 1162. 도로 포장

import sys
import heapq

input = sys.stdin.readline
INF = int(10000000000000000000000000000000000)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[INF for _ in range(k + 1)] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

def dijkstra():
  q = []
  # hour, node, count
  distance[1][0] = 0
  heapq.heappush(q, (distance[1][0], 1, 0))
  while q:
    hour, now, cnt = heapq.heappop(q)
    if distance[now][cnt] < hour: # 이미 갱신된 상태면 continue
      continue
    for i, j in graph[now]:
    # i : node, j : hour
      if cnt + 1 <= k and hour < distance[i][cnt + 1]: 
      # 포장할 때, 순서 바뀌면 index error
        distance[i][cnt + 1] = hour
        heapq.heappush(q, (distance[i][cnt + 1], i, cnt + 1))
      if hour + j < distance[i][cnt]:
      # 포장하지 않는 경우
        distance[i][cnt] = hour + j
        heapq.heappush(q, (hour + j, i, cnt))

dijkstra()
print(min(distance[n]))
