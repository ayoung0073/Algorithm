n = int(input())
ans = 0

cols = [-1 for _ in range(n)] # 각 행에 놓여진 퀸의 열 index
def solve(row):
  global ans
  if row == n:
    ans += 1
    return
  for col in range(n):
    next_is_able = True
    for before_row in range(row):
      if cols[before_row] == col or abs(before_row - row) == abs(cols[before_row] - col): # 대각선에 있는 경우
        next_is_able = False
        break
    
    if next_is_able:
     cols[row] = col
     solve(row + 1)

solve(0)
print(ans)