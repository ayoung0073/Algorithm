## 15649 N과 M

import sys 
from itertools import permutations 

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for s in list(permutations(arr, m)):
  print(' '.join(str(i) for i in s))
