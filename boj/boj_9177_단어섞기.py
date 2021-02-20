## 9177 단어섞기
import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
checks = []
for _ in range(n):
  a, b, c = input().split()
  visited = [[False for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

  q = deque([(0, 0, 0)]) # a, b, c index
  check = False
  while q:
    print(q)
    a_idx, b_idx, c_idx = q.popleft()
    if c_idx == len(c): # c의 모든 문자 거치면 True
      check = True
      break
    if len(a) > a_idx and a[a_idx] == c[c_idx] and not visited[a_idx + 1][b_idx]:
      # c의 문자와 a의 문자와 일치하는 경우
      # 방문하지 않은 idx만 만족
      q.append((a_idx + 1, b_idx, c_idx + 1))
      visited[a_idx + 1][b_idx] = True
    if len(b) > b_idx and b[b_idx] == c[c_idx] and not visited[a_idx][b_idx + 1]:
      # c의 문자와 b의 문자와 일치하는 경우
      q.append((a_idx, b_idx + 1, c_idx + 1))
      visited[a_idx][b_idx + 1] = True

  checks.append(check)
    
for i in range(len(checks)):
  if checks[i]:
    print('Data set %d: yes'%(i+1))
  else:
    print('Data set %d: no'%(i+1))
