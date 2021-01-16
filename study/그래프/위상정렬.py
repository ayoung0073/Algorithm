from collections import deque

# 노드, 간성 개수 입력 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입 차수 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기위한 연결리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보 입력 받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  # 진입 차수 1 증가
  indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
  result = [] # 알고리즘 수행 결과 담을 리스트
  q = deque() # 큐 기능을 위한 deque 라이브러리 사용

  # 처음 시작할 때는 진입차수가 0인 노드 큐에 삽입
  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    # pop 
    now = q.popleft() # 진입 차수 0인 큐에서 pop
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      # 진입 차수 0이면 enqueue
      if indegree[i] == 0:
        q.append(i)

  # 위상 정렬 수행결과 출력
  for i in result:
    print(i, end = ' ')

topology_sort()

# 시간복잡도 O(V + E)
# 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선을 차례대로 제거
