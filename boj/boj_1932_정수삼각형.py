## 1932. 정수 삼각형

import sys
input = sys.stdin.readline

n = int(input())
paths = [[] for _ in range(n)]
for i in range(n):
  paths[i] = list(map(int, input().split()))

for i in range(n - 2, -1, -1):
  for j in range(i + 1):
    paths[i][j] = max(paths[i][j] + paths[i + 1][j], paths[i][j] + paths[i + 1][j + 1])

print(paths[0][0])
