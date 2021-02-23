import sys 
input = sys.stdin.readline
n, m = map(int, input().split())
nums = []
for _ in range(n):
  nums.append(int(input()))

nums.sort()
left, right = 0, 1
result = 2000000000 #  0 ≤ |A[i]| ≤ 1,000,000,000 -> 최대 차이 : 2000000000
while left < n and right < n:
  length = nums[right] - nums[left]
  if length == m:
    result = m
    break
  elif length < m:
    right += 1
    continue
  result = min(result, length)
  left += 1

print(result)
