## 2580 스도쿠

import sys
input = sys.stdin.readline

sudoku = []
zeros = []

# 0을 찾자 
for i in range(9):
  inp = list(map(int, input().split()))
  sudoku.append(inp)
  for j in range(len(inp)):
    if inp[j] == 0:
      zeros.append((i, j))

# DFS 알고리즘으로 풀어보장,
def dfs(idx): # (확인할 zero 인덱스)
  if idx == len(zeros):
    for i in sudoku:
      print(' '.join(str(k) for k in i))
    sys.exit()
  # 가능한 숫자에 다음 인덱스 확인하기 
  zero = zeros[idx]
  for num in range(1, 10): # 확인할 숫자 num
    # 가로줄 확인
    check = True
    for i in range(9):
      if sudoku[zero[0]][i] == num:
        check = False
        break
    if not check: 
      continue
    # 세로줄 확인
    for i in range(9):
      if sudoku[i][zero[1]] == num:
        check = False
        break
    if not check: 
      continue
    # 정사각형 내 확인
    row = zero[0] // 3 # (0, 1, 2) 몫이 0이면 1~3번째 가로줄
    col = zero[1] // 3 # (0, 1, 2)
    # 0~2, 3~5, 6~8

    for i in range(row * 3, row * 3 + 3): # row * 3 + 3
      for j in range(col * 3, col * 3 + 3):
        if num == sudoku[i][j]:
          check = False
          break
      if not check: 
        break

    if not check: 
      continue
    
    sudoku[zero[0]][zero[1]] = num
    dfs(idx + 1)
    sudoku[zero[0]][zero[1]] = 0

dfs(0)
