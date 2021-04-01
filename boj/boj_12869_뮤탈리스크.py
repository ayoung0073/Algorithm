import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n = int(input())
inp = list(map(int, input().split()))

arr = [0, 0, 0]
for i in range(n): # 3개 원소로 고정
  arr[i] = inp[i]

INF = int(1e9)

dp = [[[INF for _ in range(61)] for _ in range(61)] for _ in range(61)]

q = deque([(0, arr)])

while q:
  cnt, arr = q.popleft()

  if arr[0] < 0: arr[0] = 0
  if arr[1] < 0: arr[1] = 0
  if arr[2] < 0: arr[2] = 0

  if dp[arr[0]][arr[1]][arr[2]] != INF:
    continue

  dp[arr[0]][arr[1]][arr[2]] = 0
    
  for case in list(permutations([1, 3, 9], 3)):
    q.append((cnt + 1, [arr[0] - case[0], arr[1] - case[1], arr[2] - case[2]]))
  
  dp[arr[0]][arr[1]][arr[2]] += cnt + 1

  if arr == [0, 0, 0]: break

print(dp[0][0][0] - 1)
