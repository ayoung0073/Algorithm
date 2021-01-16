# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
  if parent[x] != x: # 자기 자신이 아닌 경우, 루트 노드 존재
    parent[x] = find_parent(parent, parent[x]) # 루트노드
  return parent[x]

# 집합 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드의 개수와 간선(union 연산진행) 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용 담을 변수
edges = []
result = 0

# 부모를 자기 자신을 초기화
for i in range(1, v + 1):
  parent[i] = i

# 모든 간선에 대한 입력 받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

# 간선을 비용순으로 정렬(cost)
edges.sort()

# 간선 하나씩 확인
for edge in edges:
  cost, a, b = edge # 비용, 출발, 도착노드
  # 사이클 발생하지 않은 경우에만, 집합에 추가
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)

# 시간복잡도 : O(ElogE) - 간선을 정렬하는 작업이 가장 오래 걸림
