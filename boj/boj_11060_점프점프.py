import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
jump = list(map(int, input().split()))
visited = [True] + [False] * (n - 1)

def bfs(start):
  q = deque([start])
  while q:
    idx, cnt = q.popleft()

    if idx == n - 1:
      return cnt
    
    for i in range(1, jump[idx] + 1):
      if idx + i < n and visited[idx + i] == False:
        visited[idx + i] = True
        q.append((idx + i, cnt + 1))

  return -1

print(bfs((0, 0)))
