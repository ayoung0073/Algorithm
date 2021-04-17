## 1976 여행 가자
import sys  
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [0] * n

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a, b):
  a = find_parent(a)
  b = find_parent(b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
    
for i in range(n):
  parent[i] = i # 자기 자신으로 초기화

for i in range(n):
  arr = list(map(int, input().split()))
  for j in range(n):
    if arr[j] == 1:
      if find_parent(i) != find_parent(j):
        union_parent(i, j)

plan = list(map(int, input().split()))

comp = 0
for i in range(len(plan)):
  if i == 0:
    comp = parent[plan[0] - 1]
  elif parent[plan[i] - 1] != comp:
    print("NO")
    exit(0)
print("YES")
