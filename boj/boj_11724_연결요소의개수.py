## 11724_연결요소의 개수

### UNION
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
for _ in range(m):
  a, b = map(int, input().split())
  if a > b: # 첫번째 정점 번호를 작게 만듬
    a, b = b, a
  graph.append((a, b)) 

parent = [0] * (n + 1)
for i in range(n + 1):
  parent[i] = i

def find_parent(parent, a): # 특정 원소가 속핮 집합 찾기
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b): # 집합 합치기
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  parent[b] = a

graph.sort()

before = 0
# 간선 하나씩 확인
for edge in graph: 
  a, b = edge
  if before == find_parent(parent, a): # 처리됐던 번호(a)와 같으면 pass
    union_parent(parent, before, b)
    pass
  elif before == find_parent(parent, b):
    union_parent(parent, before, a)
    pass
  else: # 부모가 바뀌지 않았으면
    before = find_parent(parent, a)
    union_parent(parent, a, b) # 집합 합치기

print(len(set(parent)) - 1) 
# 첫번째 원소가 0이기 때문에 이것을 제외한 집합 개수 찾기



### DFS
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (n + 1)
def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      dfs(i)

result = 0

for i in range(1, n + 1):
  if not visited[i]:
    dfs(i)
    result += 1

print(result)
