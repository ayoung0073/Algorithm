# 4963. 섬의 개수
import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline 

dx = [-1, -1, -1, 1, 1, 1, 0, 0] # 왼 오
dy = [1, 0, -1, 1, 0, -1, 1, -1] # 아래 위

def dfs(a, b, arr, check):
  for i in range(8):
    x = a + dx[i] # 행
    y = b + dy[i] # 열
    if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] and check[x][y] == False:
      check[x][y] = True
      dfs(x, y, arr, check)


while True:
  w, h = map(int, input().split())
  arr = []
  check = [[False] * w for _ in range(h)]

  if (w, h) == (0, 0):
    break

  for row in range(h):
    arr.append(list(map(int, input().split())))

  ans = 0 

  for i in range(h):
    for j in range(w):
      if check[i][j] or not arr[i][j]:
        continue
      dfs(i, j, arr, check)
      ans += 1

  print(ans)
