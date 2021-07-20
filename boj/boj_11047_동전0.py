# 29200KB	68ms
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
answer = 0
for _ in range(n):
  coins.append(int(input())) # 오름차순으로 주어진다.

for i in range(n - 1, -1, -1):
  answer += k // coins[i]
  k %= coins[i]

  if k == 0: # 조건문으로 시간 단축
    break
  
print(answer)
