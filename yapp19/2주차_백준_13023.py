## 13023 ABCDE
import sys

n, m = map(int, input().split())
friends = [[] for _ in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  friends[a].append(b)
  friends[b].append(a)

visited = [False for _ in range(n)]

# 그래프의 깊이가 5이면 된다.
def dfs(idx, cnt):
  if cnt == 4: # 관계수 4
    print(1)
    sys.exit()
  for friend in friends[idx]:
    if not visited[friend]:
      visited[friend] = True
      dfs(friend, cnt + 1)
      visited[friend] = False
  
for i in range(n): # 모든 사람을 반복 
  visited[i] = True
  dfs(i, 0)
  visited[i] = False

print(0)
