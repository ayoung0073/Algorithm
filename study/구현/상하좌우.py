import time

# 공간의 크기 
n = int(input())
# 이동할 계획서
plan = list(map(str, input().split()))
start = time.time()
# 초기화
x = 0
y = 0

def check(x, y): # 범위 체크 메서드
  if x < 0 or x >= n or y < 0 or y >= n:
    return False
  else: return True

for i in plan: # O(len(plan))
  if i == 'R':
    if(check(x, y+1)):
      y += 1
  elif i  == 'L':
    if(check(x, y-1)):
      y -= 1
  elif i == 'U':
    if(check(x-1, y)):
      x -= 1
  else:
    if(check(x+1, y)):
      x += 1
me = time.time() - start
print(x+1, y+1)

n = int(input())
x, y = 1, 1
plans = input().split() # 굳이 map으로 str 안해도 됨
start = time.time()
# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

# 이동계획 하나씩 확인
for plan in plans: # O(len(plans))
  for i in range(len(move_type)): # L, R, U, D 반복
    if plan == move_type[i]:
      nx = x + dx[i]
      ny = y + dy[i]
    # 공간 벗어는 경우는 무시
  if nx < 1 or ny > 1 or nx > n or ny > n:
    continue
  # 이동 수행
  x, y = nx, ny

ans = time.time() - start
print(x, y)

print(me, ans)
print(min(me, ans)) 
    
    
