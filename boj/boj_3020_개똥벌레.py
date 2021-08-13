# 병사 배치하기
from bisect import bisect_left, bisect_right
import sys 
input = sys.stdin.readline 

n, h = map(int, input().split())
bottom = []
top = []
half = n // 2
for i in range(n):
  if i % 2 == 0:
    bottom.append(int(input()))
  else:
    top.append(int(input()))
    
bottom.sort()
top.sort() 

ans = n
count = 0
for i in range(1, h + 1):
  bottom_count = bisect_left(bottom, i - 0.5)
  top_count = bisect_left(top, h - i + 0.5)
  if n - bottom_count - top_count < ans:
    ans = n - bottom_count - top_count
    count = 1
  elif n - bottom_count - top_count == ans:
    count += 1


print(ans, count)
