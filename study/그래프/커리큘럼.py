from collections import deque
n = int(input()) # 강의 수

INF = int(1e9)

lectures = []
graph = [[] for i in range(n)]
indegree = [0] * n
time_list = [0] * n
min_time = [INF] * n

for k in range(n):
  arr = list(map(int, input().split()))
  time_list[k] = arr[0]
  for i in range(1, len(arr) - 1):
    graph[arr[i] - 1].append(k) 
    indegree[k] += 1

q = deque()

for i in range(n):
  if indegree[i] == 0: # 선수과목이 없으면(진입차수 0)
    min_time[i] = 0 # 앞 선수과목의 시간을 체크 안해도됨
    q.append(i) # 진입차수 0이면 큐에 추가

while q:
  now = q.popleft() 
  time_list[now] += min_time[now] # 진입차수가 0이 된 과목은, min_time을 합쳐서 time_list가 됨
  # print(now)
  for i in graph[now]:
    indegree[i] -= 1
    if indegree[i] == 0:
      # print(i, end = ' ')
      q.append(i)
      min_time[i] = min(min_time[i], time_list[now])

for i in time_list:
  print(i)

# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 출력결과
# 10
# 20
# 14
# 18
# 17
