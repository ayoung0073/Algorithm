## 1005 ACM Craft

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, k = map(int, input().split())
  d = [0] + list(map(int, input().split())) # 건물당 걸리는 시간

  graph = [[] for _ in range(n + 1)]
  indegree = [0] * (n + 1)
  q = deque()

  sum_val = [0] * (n + 1) # 누적 시간


  for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

  w = int(input())
  
  for i in range(1, n + 1):
    if indegree[i] == 0:
      q.append(i)
      sum_val[i] = d[i]
  
  while q:
    now = q.popleft()
    for i in graph[now]:
      sum_val[i] = max(sum_val[i], sum_val[now] + d[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  print(sum_val[w])
