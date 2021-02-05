import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

cal = []

cal += ['+'] * plus
cal += ['-'] * minus
cal += ['*'] * mul
cal += ['//'] * div

cal_list = set(permutations(cal, n - 1)) # 중복 제외

min_val = 1e9
max_val = -1e9 # 문제 잘 보기

for cal in cal_list:
  val = nums[0]
  for i in range(len(cal)):
    if cal[i] == '+':
      val += nums[i + 1]
    elif cal[i] == '-':
      val -= nums[i + 1]
    elif cal[i] == '*':
      val *= nums[i + 1]
    elif cal[i] == '//':
      if val < 0:
        val = -(abs(val) // nums[i + 1])
      else:
        val //= nums[i + 1]
  min_val = min(min_val, val)
  max_val = max(max_val, val)

print(max_val)
print(min_val)
