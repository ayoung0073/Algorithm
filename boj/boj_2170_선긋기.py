import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
arr = []
for _ in range(n):
  x, y = map(int, input().split())
  arr.append((x, y))

arr.sort()

q.append(arr[0])

for i in range(1, n):
  x, y = arr[i]
  a, b = q.popleft() # x > a는 자명(정렬된 상태)
  if x <= b:
    if y < b:
      q.appendleft((a, b))
    else:
      q.appendleft((a, y))
  else:
    if y > b:
      q.append((a, b))
      q.append((x, y))
    else:
      q.append((x, b))

res = 0
while q:
  a, b = q.popleft()
  res += b - a 

print(res)
