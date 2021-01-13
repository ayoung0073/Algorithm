# 난이도 상
# 최대한 많은 도시로 메시지를 보낸다

import heapq

INF = int(1e9) # 무한대 정의하자
n, m, c = map(int, input().split()) 
# 도시의 개수 n, 통로의 개수 m, 메시지를 보내고자 하는 도시 c
array = [[] for i in range(n)]
for _ in range(m):
  x, y, z = map(int, input().split())
  array[x - 1].append((y - 1, z)) # 튜플
  # x -> y 전달되는 시간 z

# 보낸 메시지를 받은 도시의 총 개수와 총 걸리는 시간을 출력하자

# 다익스트라인 듯하다. 
# <- 걸리는 시간이 각기 다름
# <- 시작점이 주어졌다
# -> heapq로 구현할 준비하자

q = [] # 큐 선언
distance = [INF] * n 
# INF 아닌 도시들의 개수를 구하고, 시간을 더하면 되겠다
distance[c - 1] = 0 # 시작점은 0으로 두고, heap으로 queue합시다
heapq.heappush(q, (0, c - 1))

while q:
  dist, city = heapq.heappop(q) # pop
  if dist > distance[city]: # 이미 처리했다면 무시
    continue
  for i in array[city]: # distance 갱신하자
    if distance[i[0]] > dist + i[1]:
      distance[i[0]] = dist + i[1]
      heapq.heappush(q, (distance[i[0]], i[0]))

count = 0
count_time = 0
for i in distance:
  if i != INF and i != 0:
    count += 1
    count_time = max(count_time, i) # 최대수를 구해야 함.

print(count, count_time)
