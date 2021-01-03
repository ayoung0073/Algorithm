# DFS 메서드 정의
def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True;
  print(v, end = ' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  # 방문하지 않은 노드만
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

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

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원)
visited = [False] * len(graph)  # len(graph) == 9

# dfs 메서드 호출
dfs(graph, 1, visited)

# 출력결과 : 1 2 7 6 8 3 4 5