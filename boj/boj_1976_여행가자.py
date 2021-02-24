## 1. union-find

import sys  
input = sys.stdin.readline

n = int(input())
m = int(input())

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

graph = [[] for _ in range(n)]
for i in range(n):
  info = list(map(int, input().split()))
  for j in range(len(info)):
    graph[i].append(info[j])

parent = [0] * n # 부모 테이블 초기화

# 부모를 자기 자신을 초기화
for i in range(n):
  parent[i] = i

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      union_parent(parent, i, j) # 집합 합치기

# 여행 경로 입력 받기
plan = list(map(int, input().split()))

root = find_parent(parent, plan[0] - 1)
check = True

# 여행 경로에 대한 모든 root 확인
for p in plan:
  if not root == find_parent(parent, p - 1):
     check = False
     break 

# 모든 여행 경로에 대해 root가 같으면 YES
print('YES' if check else 'NO')


## 2. 플로이드-워셜
n = int(input())  # 총 도시의 수
m = int(input())  # 여행 계획에 속한 도시들의 수
graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

# 플로이드-워셜 알고리즘을 통해 모든 노드 간의 최소 거리를 구한다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and i != j:  # 길이 없는 경우
            graph[i][j] = 1e9  # 10억으로 대입

# 최소 거리 갱신
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 여행 여부 확인
check = True
prev = plan[0] - 1
for i in range(1, m):
    if graph[prev][plan[i] - 1] >= 1e9:  # 길이 없는 경우
        check = False
        break
    else:
        prev = plan[i] - 1

if check:
    print("YES")
else:
    print("NO")
