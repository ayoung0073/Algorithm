import heapq # 우선순위큐
import sys

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split()) # 노드, 간선의 개수
start = int(input()) # 시작점

graph = [[] for i in range(n + 1)] #####
distance = [INF] * (n + 1)

for _ in range(e):
  a, b, c = map(int, input().split())
  # graph[a][b] = c # 오류
  graph[a].append((b, c)) # 튜플

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정해서, 큐에 삽입
  heapq.heappush(q, (0, start)) # (0, start) = (가중치, 노드)
  distance[start] = 0
  while q: # 큐가 비어있지 않으면 반복
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 이미 처리된 노드이면 무시
     continue
    # 현재 노드와 연결된 다른 인접한 노드 확인(갱신위함)
    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]]:
        distance[i[0]] = cost # 갱신
        heapq.heappush(q, (cost, i[0])) # 갱신하면 push

dijkstra(start)

for i in range(1, n + 1):
  if distance[i] == INF:
    print("*", end = ' ')
  else:
    print(distance[i], end = ' ')
# 시간 복잡도 O(ElogV) 
