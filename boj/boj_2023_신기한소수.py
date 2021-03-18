import sys
import math
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(['2', '3', '5', '7'])

def is_prime(num):
  for i in range(2, int(math.sqrt(num) + 1)):
    if num % i == 0:
      return False
  return True

while q:
  if len(q[0]) == n:
    break
  str_num = q.popleft()
  # 소수 판별 시작
  for i in range(1, 10, 2):
    if is_prime(int(str_num + str(i))):
      q.append(str_num + str(i))

for i in q:
  print(i)
