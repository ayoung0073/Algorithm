# 14502. 연구소
import sys
import copy

input = sys.stdin.readline
n, m = map(int, input().split())
result = 0
maps = []
temp = [[0 for j in range(m)] for i in range(n)]

for _ in range(n):
  tmp = list(map(int, input().split()))
  maps.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y): # x, y 좌표의 상하좌우 바이러스 퍼뜨리기
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        temp[nx][ny] = 2 # 바이러스 전염
        virus(nx, ny) # 재귀 함수 호출

def max_area(): 
  area = 0
  for i in range(n):
    # for j in range(m):
    #   if temp[i][j] == 0:
    #     area += 1
    area += temp[i].count(0)
  return area
# 벽 설치한 뒤 리스트
# dfs를 이용해 벽을 설치하면서, 매번 안전 영역 크기 계산
def dfs(count):
  global result # 리턴값
  global temp

  if count == 3: # 벽 3개 모두 설치한 경우
    temp = copy.deepcopy(maps) # global 선언 해줘야 함
    # for i in range(n):
    #   for j in range(m):
    #     temp[i][j] = maps[i][j]
    
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    result = max(result, max_area())

    return

  # 빈 공간에 벽 설치
  for i in range(n):
    for j in range(m):
      if maps[i][j] == 0:
        maps[i][j] = 1
        count += 1
        dfs(count)
        maps[i][j] = 0
        count -= 1
  
dfs(0)
print(result)
