## 18352. 특정 거리의 도시 찾기
from collections import deque
import sys

input = sys.stdin.readline
n, m, k, x = map(int, input().split()) 
# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호

roads = [[] for _ in range(n)]

for _ in range(m):
  a, b = map(int, input().split())
  roads[a - 1].append(b - 1)
  
distance = [0 for _ in range(n)]
visited = [False] * n
result = []

def bfs(x):
  q = deque([x]) # deque 모듈
  visited[x] = True
  while q:
    obj = q.popleft()
    for road in roads[obj]:
      if visited[road] == False:
        visited[road] = True
        distance[road] += distance[obj] + 1
        q.append(road)
  

bfs(x - 1)

check = False
for i in range(len(distance)):
  if distance[i] == k:
    print(i + 1)
    check = True

if check == False: # 최단 거리 k가 존재하지 않을 때
  print(-1)
