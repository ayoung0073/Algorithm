# 수평 두칸 & 수직 1칸
# 수직 두칸 & 수평 1칸 가능

# a의 아스키코드값은 97

d_col = [-2, -2, 2, 2, -1, -1, 1, 1] # col 변화량
d_row = [1, -1, 1, -1, 2, -2, 2, -2] # row 변화량

row, col = input()

row = ord(row) - 97 + 1 # 숫자로 바꾸었다
col = int(col)

count = 0
for i in range(8):
  r = row + d_row[i]
  c = col + d_col[i]
  if r < 1 or r > 8 or c < 1 or c > 8:
    continue
  else:
    count += 1

print(count)


# 답
input_data = input()
row = int(input_data[1]) # 문자열 나눔
col = ord(input_data[0]) - ord('a') + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
# 상하좌우 문제에서는 dx, dy 리스트를 선언하여 이동할 방향 기록(내방법)
# BUT 이 문제는 steps 변수로 대신 수행 # 튜플
steps = [(2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2) , (-2, 1)]

count = 0
for step in steps:
  # 이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_col = col + step[1]

  if next_row >=1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
    count += 1

print(count)
