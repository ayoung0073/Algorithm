# 간단한 다익스트라 알고리즘
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미(10억)

# 노드의 개수, 간선의 개수 입력 받기
n, e = map(int, input().split())
# 시작 노드 번호 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 담기
graph = [[] for i in range(n + 1)] # n + 1 !!!
# 방문한 적이 있는지 체크하는 리스트
visited = [False] * (n + 1)
# 최단 거리 테이블
# 계속 갱신할 리스트
distance = [INF] * (n + 1)

# 모든 간선 정보 입력 받기
for _ in range(e): # 간선의 개수만큼 입력 받기
  a, b, c = map(int, input().split()) # a -> b로 가는 가중치 c
  graph[a].append((b, c)) # 튜플

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
# distance 로 비교
def get_smallest_node():
  min_value = INF
  index = 0 # 가장 짧은 노드 인덱스
  for i in range(1, n + 1): # 1 ~ n 노드에서 찾기
    if distance[i] > min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  visited[start] = True
  distance[start] = 0
  for j in graph[start]:
    distance[j[0]] = j[1]
  # 시작 노드를 제외한 전체 (n - 1)개의 노드에 대해 반복
  for i in range(n - 1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리
    now = get_smallest_node() # 현재 노드 설정
    visited[now] = True
    # 현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
      # 최단 경로 갱신하자
      cost = distance[now] + j[1]
      # 현재 노드 + 가중치 가 더 짧은 경우
      if cost < distance[j[0]]:
        distance[j[0]] = cost # 갱신

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
  # 도달할 수 없는 경우 INF 출력
  if distance[i] == INF:
    print('*')
  else:
    print(distance[i])
