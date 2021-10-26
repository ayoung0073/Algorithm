## 9576 책 나눠주기

import sys 
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  demand = [] 
  check = [False] * (n + 1) # 줬는지 체크하는 배열
  count = 0 # 최대 학생 수 
  for _ in range(m):
    demand.append(list(map(int, input().split())))
  demand.sort(key = lambda x:x[1]) # b를 기준으로 오름차순 정렬

  for a, b in demand:
    for i in range(a, b + 1):
      if not check[i]:
        check[i] = True
        count += 1
        break
  print(count)
