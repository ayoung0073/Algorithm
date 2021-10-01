## 2075 N번째 큰 수

import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = []
q = []

for _ in range(n):
  graph.append(list(map(int, input().split())))

for i in range(n):
  heapq.heappush(q, ((-1) * graph[n - 1][i], (n - 1, i)))

idx = 0

while idx != n - 1:
  idx += 1
  x, y = heapq.heappop(q)[1]
  if x >= 1:
    heapq.heappush(q, ((-1) * graph[x - 1][y], (x - 1, y)))

print((-1) * heapq.heappop(q)[0])
