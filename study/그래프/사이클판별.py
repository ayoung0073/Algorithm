# union-find 자료구조 (합치기찾기 자료구조)

# 경로 압축(Path compression) 
# find 함수를 재귀적으로 호출한 뒤, 부모 테이블값을 갱신하자.
# 가장 루트노드로, 부모 테이블 값을 갱신하자
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x]) # 갱신
  return parent[x]

# 두 원소가 속한 집합을 찾고(find_parent), 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b: # 작은 원소가 루트 노드가 됨
    parent[b] = a
  else:
    parent[a] = b

# 노드 개수, 간선 개수(union 연산) 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

for i in range(1, v + 1):
  parent[i] = i # 부모 테이블 부모를 자기 자신으로 초기화

cycle = False

# union 연산
for i in range(e): # 간선의 개수만큼 반복
  a, b = map(int, input().split())
  # 사이클 발생할 경우, 종료
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  # 사이클 발생하지 않았을 경우, union 연산 수행
  else:
    union_parent(parent, a, b)

if cycle:
  print('사이클 발생 O')
else:
  print('사이클 발생 X')
