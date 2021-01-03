# 공백 구분해서 입력 받음
n, m = map(int, input().split()) # 외우쟈...

# 2차원 리스트의 맵 정보를 입력 받음
graph = []
for i in range(n):
  # 정수로 입력 받은 것을 list로
  # split을 하면 공백을 구분해서 입력받음(지금은 한자리수이므로 안해도 됨)
  data = list(map(int, input()))
  graph.append(data)

def dfs(x, y):
  if x >= n or x < 0 or y >= m or y < 0:
    return False
  if(graph[x][y] == 0):
    graph[x][y] = 1
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    return True
  return False

result = 0

for i in range(n):
  for j in range(m):
    if(dfs(i, j)):
      result += 1
print(result)
