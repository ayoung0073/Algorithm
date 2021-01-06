n, m = map(int, input().split())
a, b, d = map(int, input().split())
# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
#data = [[0] for range(m) for range(n)]

dx = [0, 1, 0, -1] # x축 변화량
dy = [-1, 0, 1, 0] # y축 변화량
visited = [[False]*m for _ in range(n)]
data = []
for i in range(n): # 세로 길이만큼 입력 반복4 4 
  data.append(list(map(int, input().split())))
  #print(data[i][1])

def check_range(x, y): # 갈수 있는 범위인지 체크
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  elif data[x][y] == 1 or visited[x][y] == True:
    return False
  return True

# if d == 0: idx = 3
# elif d == 1: idx = 0
# elif d == 2: idx = 1
# elif d == 3 : idx = 2

# 4 더하고 3으로 나눈 나머지 
result = 1
count = 0

idx = d - 1
while True:
  if idx == -1:
    idx += 4
  if check_range(a + dx[idx], b + dy[idx]):
    a += dx[idx]
    b += dy[idx]
    visited[a][b] =  True
    result += 1
    count = 0
  else:
    count += 1
  if count == 4: break
  idx -= 1

print(result)
    
