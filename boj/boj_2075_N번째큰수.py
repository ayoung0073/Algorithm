import sys 
import heapq

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
  arr.append(list(map(int, input().split())))

# 마지막 행 heappush(마지막 행에 가장 큰 수 존재)
q = []
for i in range(n):
  heapq.heappush(q, ((-1) * arr[n - 1][i], (n - 1, i)))

idx = 0
while idx != n - 1:
  idx += 1
  now = heapq.heappop(q)[1] # 좌표 꺼내기
  if now[0] == 0:
    break
  heapq.heappush(q, ((-1) * arr[now[0] - 1][now[1]], (now[0] - 1, now[1]))) # 자기보다 작은 위의 수 push
print((-1) * heapq.heappop(q)[0])
