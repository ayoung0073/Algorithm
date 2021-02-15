import sys 
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
bus_info = [[INF for _ in range(n)] for _ in range(n)]

for i in range(n):
  bus_info[i][i] = 0
for _ in range(m):
  a, b, c = map(int, input().split())
  bus_info[a - 1][b - 1] = min(bus_info[a - 1][b - 1], c)

for k in range(n):
  for i in range(n):
    for j in range(n):
      bus_info[i][j] = min(bus_info[i][j], bus_info[i][k] + bus_info[k][j])

for bus in bus_info:
  for i in bus:
    if i == INF:
      print(0, end = ' ')
    else:
      print(i, end = ' ')
  print()
