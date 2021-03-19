## 16197 두 동전

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split()) # 세로, 가로
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
board = []
q = []
coin = []
for i in range(n):
  arr = list(map(str, input().rstrip()))
  board.append(arr)
  for j in range(len(arr)):
    if board[i][j] == 'o':
      coin.append((i, j))
heapq.heappush(q, (0, coin))
visited[coin[0][0]][coin[0][1]][coin[1][0]][coin[1][1]] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def check_range(x, y):
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  return True

def bfs(q):
  while q: # 2개씩
    cnt, coin_set = heapq.heappop(q)
    coin1 = coin_set[0]
    coin2 = coin_set[1]

    if cnt >= 10:
      return -1

    for i in range(4):
      next_coin1 = (coin1[0] + dx[i], coin1[1] + dy[i])
      next_coin2 = (coin2[0] + dx[i], coin2[1] + dy[i])

      if not check_range(next_coin1[0], next_coin1[1]) and not check_range(next_coin2[0], next_coin2[1]):
        continue
      
      # 하나만 떨어지는 경우 return cnt + 1
      if (check_range(next_coin1[0], next_coin1[1]) and not check_range(next_coin2[0], next_coin2[1])) or (not check_range(next_coin1[0], next_coin1[1]) and check_range(next_coin2[0], next_coin2[1])):
        return cnt + 1
      
      if board[next_coin1[0]][next_coin1[1]] =='#': # 벽인 경우
        next_coin1 = coin1
      if board[next_coin2[0]][next_coin2[1]] =='#': # 벽인 경우
        next_coin2 = coin2
      
      # print(visited[next_coin1[0]][next_coin1[1]][next_coin2[0]][next_coin2[1]])
      if not visited[next_coin1[0]][next_coin1[1]][next_coin2[0]][next_coin2[1]]:
        visited[next_coin1[0]][next_coin1[1]][next_coin2[0]][next_coin2[1]] = True
        heapq.heappush(q, (cnt + 1, (next_coin1, next_coin2)))
      
  return -1

print(bfs(q))
