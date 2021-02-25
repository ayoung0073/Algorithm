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
