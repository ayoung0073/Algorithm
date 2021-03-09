import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, x, y):
  x = find_parent(parent, x)
  y = find_parent(parent, y)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x

while True:
  m, n = map(int, input().split())
  if m == 0 and n == 0:
    break
  edges = []
  parent = [0] * n
  for _ in range(n):
    x, y, z = map(int, input().split())
    edges.append((z, x, y)) # cost(거리), x, y


  edges.sort() # cost 순으로 정렬

  for i in range(len(parent)):
    parent[i] = i # 초기화

  res = 0
  for cost, x, y in edges:
    if find_parent(parent, x) != find_parent(parent, y): # 집합 합침
      union_parent(parent, x, y)
    else:
      res += cost

  print(res)
