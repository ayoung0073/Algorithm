# 길의 유지비 합 최소로 구하기

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arrays = []
result = 0 # 없애고 남은 길 유지비 합
parent = [0] * (n + 1) # 부모테이블 
for i in range(n + 1):
  parent[i] = i  # 부모테이블 자기 자신으로 초기화

for _ in range(m):
  a, b, c = map(int, input().split())
  # a번 집과 b번 집을 연결하는 길의 유지비 c
  arrays.append((a, b, c))

def sort_cost(arr):
  return arr[2]

arrays.sort(key = sort_cost) # 유지비용 기준으로 오름차순 정렬
# print(arrays)

def find_parent(parent, a): # 자신이 속한 집합 찾기(루트노드)
  if parent[a] != a: # 자기 자신이 루트 노드가 아니라면
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b): # 집합 합치기
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

for i in arrays:
  a, b, c = i
  if find_parent(parent, a) != find_parent(parent, b):
   # 서로 집합이 다르면 합치기
   union_parent(parent, a, b)
   result += c
   last = c

print(result - last)
# result 는 모든 집이 한 마을에 있는 것, 
# 두 마을로 나누고 유지비합이 최소가 되려면 가장 큰 비용의 길을 다른 마을로 바꾸면 됨
