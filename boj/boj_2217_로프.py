import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
val = 0
for _ in range(n):
  heapq.heappush(arr, int(input()))

while arr:
  w = heapq.heappop(arr)
  val = max(val, w * n)
  n -= 1
  
print(val)
