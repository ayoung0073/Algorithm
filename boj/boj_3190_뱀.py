## 3190. 뱀
from collections import deque
import sys

input = sys.stdin.readline

n = int(input()) # 보드의 크기
board = [[0 for col in range(n)] for row in range(n)]

k = int(input())

apples = []
for _ in range(k): # 사과 위치 입력 받기
  r, c = map(int, input().split()) 
  board[r - 1][c - 1] = 1

l = int(input()) # 뱀 방향 변환 횟수
directions = dict()

for _ in range(l): # 방향 변환 정보 입력 받기
  x, c = input().split()
  directions[int(x)] = c

# 0 : 사과 존재 X
# 1 : 사과 존재 O
# 2 : 뱀 존재 

dc = [1, 0, -1, 0] 
dr = [0, 1, 0, -1]  # 우 하 좌 상

idx = 0 # 방향 변수(+1 : 오른쪽, -1 : 왼쪽)
r = c = 0

second = 0

q = deque([(0, 0)]) # 뱀이 지나간 곳 저장하자 # tail 계속 바뀜
def check_range(length, r, c):
  if r < 0 or c < 0 or r >= length or c >= length:
    return False
  else: return True

while True:
  # 1초뒤 이동할 좌표가 부딪히거나 자기 몸에 부딪혔을 때 
  tmp_r = r + dr[idx]
  tmp_c = c + dc[idx]
  if not check_range(n, tmp_r, tmp_c) or board[tmp_r][tmp_c] == 2:
    print(second + 1)
    break
  else:
    second += 1
    r, c = tmp_r, tmp_c
    q.append((r, c))
    if  board[r][c] == 1: # 사과가 있는 경우
      pass

    else: 
      # 꼬리 저장할 변수 필요하군(리스트? 큐?) 큐!
      tail = q.popleft() # 꼬리 이동
      board[tail[0]][tail[1]] = 0
    
    board[r][c] = 2

    # 방향 전환 체크
    if second in directions.keys():
      if directions[second] == 'L':
        idx = (idx - 1) % 4
      else:
        idx = (idx + 1) % 4
