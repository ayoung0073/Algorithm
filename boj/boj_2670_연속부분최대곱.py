n = int(input())
arr = []

for _ in range(n):
  arr.append(float(input()))

ans = 0

for i in range(n):
  mul = 1
  for j in range(i, n):
    mul *= arr[j]
    ans = max(mul, ans)
  
print('%.3f'%(ans))
