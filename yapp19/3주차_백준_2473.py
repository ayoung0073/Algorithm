## 2473. 세 용액 

import sys
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))

answer = []
near_val = sys.maxsize

values.sort()

for i in range(n - 2):
  l = i + 1
  r = n - 1
  while l < r:
    sum_val = values[i] + values[l] + values[r]
    if near_val >= abs(sum_val):
      answer = [values[i], values[l], values[r]]
      near_val = abs(sum_val)
    if sum_val < 0:
      l += 1
    elif sum_val > 0: 
      r -= 1
    else:
      print(values[i], values[l], values[r])
      sys.exit()
      
print(answer[0], answer[1], answer[2])
