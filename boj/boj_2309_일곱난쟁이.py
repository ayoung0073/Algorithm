# 이중 for문 풀이
# 29200KB	68ms
import sys
input = sys.stdin.readline

arr = []

for _ in range(9):
  arr.append(int(input()))
sum_height = sum(arr)

ans = []
for i in range(8):
  for j in range(i + 1, 9):
    if sum_height - arr[i] - arr[j] == 100:
      for k in range(9):
        if k != i and k != j:
          ans.append(arr[k])
      print('\n'.join(str(i) for i in sorted(ans)))
      exit(0)
      
      
# itertools combination 풀이
# 29200KB	68ms
from itertools import combinations
import sys
input = sys.stdin.readline

arr = []

for _ in range(9):
  arr.append(int(input()))
sum_height = sum(arr)

for comb in combinations(arr, 7):
  if sum(comb) == 100:
    print('\n'.join(str(i) for i in sorted(comb)))
    exit(0)
