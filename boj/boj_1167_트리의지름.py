## 트리의 지름
from collections import deque
import sys

input = sys.stdin.readline
v = int(input())

graph = [[] for i in range(v + 1)]
data = []
for _ in range(v):
  data = list(map(int, input().split()))
  vertex = data[0] # index error 발생
  j = 1

  for _ in range((len(data) - 2)//2):
    graph[vertex].append((data[j], data[j + 1]))
    j += 2
result = 0

def bfs(x):
  visited = [False] * (v + 1)
  distance = [0] * (v + 1)

  q = deque(graph[x]) # 튜플 리스트

  for k in graph[x]:
    #print(k)
    if not visited[k[0]]:
      visited[k[0]] = True
      distance[k[0]] = k[1]
  #print(graph[i])
  visited[x] = True

  while q:
    now, cost = q.popleft()
    for k in graph[now]:
      if not visited[k[0]]:
        visited[k[0]] = True
        q.append(k)
        distance[k[0]] = max(distance[now] + k[1], distance[k[0]])

  max_idx = 0
  for i in range(1, len(distance)):
    if distance[max_idx] < distance[i]:
      max_idx = i
  
  return max_idx, distance[max_idx]

idx, val = bfs(1)
print(bfs(idx)[1])
# bfs
