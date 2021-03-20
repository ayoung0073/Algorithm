## 9470. Strachler 순서

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  k, m, p = map(int, input().split())

  graph = [[] for _ in range(m + 1)]
  indegree = [0] * (m + 1)

  order = [0] * (m + 1)
  order_max = [[0, 0] for _ in range(m + 1)]

  for _ in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

  q = deque()
  for i in range(1, m + 1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    num = q.popleft()
    if order_max[num][1] == 1:
      order[num] = order_max[num][0]
    else:
      order[num] = order_max[num][0] + 1
    
    for i in graph[num]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)
      
      if order_max[i][0] < order[num]:
        order_max[i][0] = order[num]
        order_max[i][1] = 1
      elif order_max[i][0] == order[num]:
        order_max[i][1] += 1

  print(k, order[m])
