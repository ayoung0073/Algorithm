# 29200KB 428ms

import sys
from itertools import combinations
input = sys.stdin.readline 

n, s = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for num in range(1, n + 1): 
  for sub_arr in combinations(arr, num):
    if sum(sub_arr) == s:
      answer += 1

print(answer)
