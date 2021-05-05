## 숨바꼭질
import heapq
n, k = map(int, input().split())

INF = int(1e9)
visited = [False] * 100001
q = [(0, n)] # second, now
visited[n] = True
 
while q:
  second, now = heapq.heappop(q)
  if now == k:
    print(second)
    break
  
  if now * 2 <= 100000 and not visited[now * 2]:
    visited[now * 2] = True
    heapq.heappush(q, (second + 1, now * 2))
  if now  + 1 <= 100000 and not visited[now + 1]:
    visited[now + 1] = True
    heapq.heappush(q, (second + 1, now + 1))
  if now - 1 >= 0 and not visited[now - 1]:
    visited[now - 1] = True
    heapq.heappush(q, (second + 1, now - 1))
