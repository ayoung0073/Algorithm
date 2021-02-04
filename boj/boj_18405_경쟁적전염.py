from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
virus_list = []
exists = []
virus_cnt = 0

visited = [[False for _ in range(n)] for _ in range(n)] 

for i in range(n):
  tmp = list(map(int, input().split()))
  for j in range(n):
    if tmp[j] != 0:
      virus_cnt += 1 # 바이러스 수 
      exists.append((tmp[j], i, j)) # 번호, 행, 열
      visited[i][j] = True
  virus_list.append(tmp)

s, x, y = map(int, input().split())
exists.sort() # 낮은 번호 순으로 정렬
q = deque(exists)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


cnt = 0
second = 0
while q and second != s:
  out = q.popleft()
  cnt += 1
  # 상하좌우 체크
  for i in range(4):
    nx = out[1] + dx[i]
    ny = out[2] + dy[i]

    if nx >= 0 and ny >= 0 and nx < n and ny < n: # 범위 체크
      cnt += 1
      if virus_list[nx][ny] == 0:
        virus_list[nx][ny] = out[0]
        q.append((virus_list[nx][ny], nx, ny))
      elif virus_list[nx][ny] == out[0]:
        continue
      elif visited[nx][ny] == False:
        q.append((virus_list[nx][ny], nx, ny))
      else: continue
      visited[nx][ny] = True

  if cnt == virus_cnt:
    second += 1
print(virus_list[x - 1][y - 1])
