import sys  
input = sys.stdin.readline

res = []
t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  max_val = 0
  ans = 0
  for i in range(n - 1, -1 ,-1):
    if arr[i] > max_val:
      max_val = arr[i]
    else:
      ans += (max_val - arr[i])
  print(ans)

  
### 21.07.30  풀이 추가
  
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split())) # 날 별 주가 

  ans = 0
  max_idx = n - 1 
  
  for i in range(n - 2, -1, -1): 
    if arr[i] > arr[max_idx]:
      for j in range(i + 1, max_idx):
        ans += arr[max_idx] - arr[j]
      max_idx = i

  if max_idx > 0:
    for i in range(0, max_idx):
      ans += arr[max_idx] - arr[i]
  
  print(ans)
