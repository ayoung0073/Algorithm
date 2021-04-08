import sys
import heapq

input = sys.stdin.readline
t = int(input())
for _ in range(t):
  k, m, p = map(int, input().split())
  parent = [0] * (m + 1)
  arr = [0] * (m + 1)
  graph = [[] for _ in range(m + 1)]
  dp = [[0] * 1001 for _ in range(1001)]

  for _ in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    parent[b] += 1

  q = []

  for i in range(1, len(parent)):
    if parent[i] == 0: 
      heapq.heappush(q, (1, i))
      arr[i] = 1
  
  while q:
    cnt, now = heapq.heappop(q)
    for i in graph[now]:
      parent[i] -= 1

      if dp[i][1] != cnt:
        dp[i][1] = max(dp[i][1], cnt)
      elif dp[i][1] == cnt:
        dp[i][2] = max(dp[i][2], cnt)

      if parent[i] == 0: 
        arr[i] = max(dp[i][2] + 1, dp[i][1])
        heapq.heappush(q, (arr[i], i))

  print(k, arr[m])
