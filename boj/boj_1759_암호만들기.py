from itertools import combinations
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
arr = list(map(str, input().split()))
ans = []

for sub_string in combinations(arr, l):
  v = False
  c = 0
  for ch in sub_string:
    if ch in 'aeiou':
      v = True
    else:
      c += 1
  if v and c >= 2:
    ans.append(sorted(sub_string))

ans.sort()
for i in ans:
  print(''.join(i))
