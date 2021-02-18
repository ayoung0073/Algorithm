## 9370. 미확인 도착지
import sys 
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
  distance = [INF] * (n + 1)
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start)) # 출발지
  while q:
    dist, now = heapq.heappop(q) 
    if dist > distance[now]: # 이미 갱신한 상태
      continue
    for j in graph[now]:
      a, b = j # 도착지, 거리
      if distance[a] > dist + b:
        distance[a] = dist + b
        heapq.heappush(q, (distance[a], a))
  return distance
  
T = int(input())
for _ in range(T):
  n, m, t = map(int, input().split())
  # n : 교차로, m : 도로, t : 목적지 후보 개수
  s, g, h = map(int, input().split())
  # s : 출발, g, h : 교차로

  graph = [[] for _ in range(n + 1)] # 양방향 도로
  for _ in range(m): 
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
    if (a, b) == (g, h) or (b, a) == (g, h):
      path_g_h = d

  dest = []
  for _ in range(t):
    dest.append(int(input()))

  dest.sort()
  
  # 목적지 후보 중 g, h 사이를 지나야함
  dist_s = dijkstra(s, graph, n) # 시작점 > 모든 노드
  dist_g = dijkstra(g, graph, n) # g > 모든 노드
  dist_h = dijkstra(h, graph, n) # h > 모든 노드 

  path_s_g = dist_s[g] # 시작점에서 g까지의 최단 거리
  path_s_h = dist_s[h] 

  answer = []
  for i in dest:
    if dist_s[i] == path_s_g + path_g_h + dist_h[i] or dist_s[i] == path_s_h + path_g_h + dist_g[i]:
      answer.append(i)

  print(' '.join(map(str, answer)))
