from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # start를 enqueue한 채로 queue 생성
  queue = deque([start])
  # 시작 노드 방문 처리
  visited[start] = True
  while queue: # 큐가 empty면 종료
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * len(graph)

bfs(graph, 1, visited)

# 출력결과 : 1 2 3 8 7 4 5 6 