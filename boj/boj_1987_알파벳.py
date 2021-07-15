import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [[] for _ in range(r)]
for row in range(r):
    board[row] = list(input().strip())

def check_range(row, col):
  if r > row and row >= 0 and c > col and col >= 0:
    return True
  return False

ans = 0
x = [1, 0, -1, 0]
y = [0, 1, 0 , -1]
# 백트랙킹 시작 
q = set()
q.add(((0, 0), board[0][0]))
while q:
  now, check = q.pop()
  ans = max(len(check), ans)
  sub_check = set()
  for i in range(4):
    next_r = now[0] + x[i] 
    next_c = now[1] + y[i] 
    if check_range(next_r, next_c):
      if board[next_r][next_c] not in check:
        q.add(((next_r, next_c), check + board[next_r][next_c]))

print(ans)
