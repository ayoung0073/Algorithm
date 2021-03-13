import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  p = input().rstrip() # 수행할 함수
  n = int(input())
  tmp = input().rstrip().replace('[', '').replace(']', '')
  if n > 1:
    arr = deque(list(map(int, tmp.split(','))))
  elif n == 1:
    arr = deque([int(tmp)])
  else:
    arr = deque([])

  error = False
  r_cnt = 0
  for i in p:
    if i == 'R':
      r_cnt += 1
    else: # 삭제하는 경우
      if len(arr) == 0:
        print('error')
        error = True
        break
      else:
        if r_cnt % 2 == 0:
          arr.popleft()
        else:
          arr.pop()

  if r_cnt % 2 == 1:
    arr.reverse()
  if not error:
    print("[", end="")
    for i in range(len(arr)):
        if i == len(arr) - 1:
            print(arr[i], end="")
        else:
            print(str(arr[i]) + ",", end="")
    print("]")

