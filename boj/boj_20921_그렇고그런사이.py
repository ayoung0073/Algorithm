import sys 
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

tmp = [i for i in range(n, 0, -1)]
q = deque(tmp)
ans = []
while True:
  num = q.popleft()
  if num - 1 > k:
    q.append(num)
    continue
  elif num - 1 == k:
    ans.append(num)
    ans += sorted(list(q))
    break
  else:
    ans.append(num)
    k -= (num - 1)

if ans:
  print(' '.join(str(ans[i]) for i in range(len(ans))))
else:
  ans = [i for i in range(1, n + 1)]
  print(' '.join(str(ans[i]) for i in range(len(ans))))
