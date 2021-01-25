## 15953. 상금 헌터
import sys

input = sys.stdin.readline
t = int(input())

fest1 = [
  (22, 0),
  (16, 100000),
  (11, 300000),
  (7, 500000),
  (4, 2000000),
  (2, 3000000),
  (1, 5000000)
]

fest2 = [
  (32, 0),
  (16, 320000),
  (8, 640000),
  (4, 1280000),
  (2, 2560000),
  (1, 5120000)
]

for _ in range(t):
  result = 0
  a, b = map(int, input().split())
  
  for first in fest1:
    if first[0] <= a:
      result += first[1]
      break
      
  for second in fest2:
    if second[0] <= b:
      result += second[1]
      break

  print(result)
