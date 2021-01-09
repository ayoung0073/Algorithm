import sys

n = int(input())
req = list(map(int, sys.stdin.readline().rstrip().split()))
all = int(input())

# 처음 초기화한 upper * n은 all을 넘지 않음
upper = all // n

def assign(req, upper):
  sum = 0
  for i in req:
    if i >= upper:
      sum += upper
    else:
      sum += i
  return sum

# 총 예산이 배정된 예산의 합보다 클 때, 반복문 종료
if sum(req) <= all:
  print(max(req))
else:
  while True:
    if assign(req, upper) < all:
      upper += 1
    elif assign(req, upper) == all:
      break
    else:
      upper -= 1
      break
  print(upper)
