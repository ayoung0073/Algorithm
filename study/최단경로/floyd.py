INF = int(1e9) # 무한을 의미하는 값으로 10억 

# 노드, 간선의 개수
n = int(input())
m = int(input())

# 2차원 리스트(그래프 표현)을 만들고, 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2차원으로 가능
# graph = [[] for i in range(n + 1)] -> 튜플이고

# 자기 자신의 비용은 0으로 
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

# 간선의 정보 입력 받기
for _ in range(e):
    # A에서 B로 가는 비용 C
    a, b, c = map(int, input().split())
    graph[a][b] = c 
    # graph = [[] for i in range(n + 1)] 
    # 만약 이런 graph를 선언했으면 오류 index

# 점화식에 따라 플로이드 알고리즘 수행
#  O(N^3)
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print('*', end = ' ')
    else:
      print(graph[a][b])
  print()
