## 13308. 주유소
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cost = [0] + list(map(int, input().split()))
info = [[] for _ in range(n + 1)] 
visited = [[False for _ in range(2501)] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  info[a].append((b, c))
  info[b].append((a, c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, (start, cost[start]))) # 현재까지의 주유 가격, (출발할 다음 노드 번호, 다음 노드에서 쓸 주유 리터당 가격)

  while q:
    cst, now = heapq.heappop(q) 

    if now[0] == n: # 현재 노드 번호가 n번이면 종료(heapq 정렬이기 때문에, 가장 적은 cost값)
      return cst

    if visited[now[0]][now[1]]: # 해당 주유리터당 가격으로 현재 노드를 이미 방문한 경우 continue
      continue

    visited[now[0]][now[1]] = True # 방문 처리

    min_cost = min(now[1], cost[now[0]])
    for i in info[now[0]]:
      if visited[i[0]][min_cost]: # 조건 체크!!
        continue
      total = cst + i[1] * min_cost 
      heapq.heappush(q, (total, (i[0], min_cost)))

  return -1

print(dijkstra(1))
