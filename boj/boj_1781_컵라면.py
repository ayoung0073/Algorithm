import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []
q = []

for _ in range(n):
  deadline, num = map(int, input().split())
  arr.append((deadline, num))

arr.sort(key = lambda x : (x[0]))

for deadline, num in arr:
  if deadline > len(q):
    heapq.heappush(q, num)
  else:
    num_comp = heapq.heappop(q)
    if num_comp >= num:
      heapq.heappush(q, num_comp)
    else:
      heapq.heappush(q, num)

print(sum(q))
