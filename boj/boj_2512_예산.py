## 예산

import sys
input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
all_val = int(input())

left = 0
right = max(requests) 

ans = 0

while left <= right:
  upper = (left + right) // 2
  sum_val = 0
  for request in requests:
    if request < upper:
      sum_val += request
    else:
      sum_val += upper
      
  if sum_val == all_val:
    print(upper)
    exit(0)
  elif sum_val > all_val:
    right = upper - 1
  else:
    left = upper + 1
    ans = upper

print(ans)
