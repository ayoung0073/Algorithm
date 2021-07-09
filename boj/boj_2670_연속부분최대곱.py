import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(float(input()))

max_val = max(arr)
for i in range(n - 1):
  mul_val = arr[i]
  for j in range(i + 1, n):
    mul_val *= arr[j]
    max_val = max(mul_val, max_val)

print('%.3f'%(max_val))
