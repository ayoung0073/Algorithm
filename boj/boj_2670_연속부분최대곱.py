import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
  arr.append(float(input()))

max_val = max(arr)
for i in range(n - 1):
  mul_val = 1
  sub_max_val = arr[i]
  for j in range(i, n):
    mul_val *= arr[j]
    sub_max_val = max(mul_val, sub_max_val)
  max_val = max(sub_max_val, max_val)

print('%.3f'%max_val)
