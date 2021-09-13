## 2668 숫자 고르기

arr = [0]
n = int(input())
for _ in range(n):
  arr.append(int(input()))

visited = [False for _ in range(n + 1)]
result = []

def dfs(now, idx):  
  visited[now] = True
  if not visited[arr[now]]:
    dfs(arr[now], idx)
  elif arr[now] == idx: # cycle인 경우
    result.append(arr[now])

for i in range(1, n + 1):
  visited = [False for _ in range(n + 1)] # 반복할 때마다 초기화
  dfs(i, i)

print(len(result))
for i in result:
  print(i)
