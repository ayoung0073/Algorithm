### 2887. 행성 터널
import sys 
input = sys.stdin.readline

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

n = int(input())

parent = [0] * n # 부모 테이블 초기화
for i in range(n):
  parent[i] = i

planets = []
edges = []

result = 0

for i in range(n):
  a, b, c = map(int, input().split())
  planets.append((a, b, c, i))

for i in range(3):
  planets.sort(key=lambda x:x[i])
  for j in range(1, n):
    edges.append((abs(planets[j - 1][i] - planets[j][i]), planets[j - 1][3], planets[j][3]))

edges.sort()
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
