import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

graph = [[] for i in range(n)] 
# 튜플로 추가할 것

for i in range(m):
  a, b, c = map(int, input().split())
  graph[a - 1].append((b - 1, c))
  # 출발도시에 (도착도시, 비용) 추가

distance = [INF] * n
start, end = map(int, input().split())
# 출발도시, 도착 도시
q = [] # 힙 큐
heapq.heappush(q, (0, start - 1))
# 0: 거리, start: 노드 번호
while q:
  dist, now = heapq.heappop(q)
  if dist > distance[now]: # 이미 처리된 경우 pass
    continue
  for i in graph[now]:
    cost = dist + i[1] # 현재 선택된 노드에서의 거리 구하기
    if cost < distance[i[0]]: # distance 갱신 조건
      distance[i[0]] = cost
      heapq.heappush(q, (cost, i[0]))

print(distance[end - 1])
