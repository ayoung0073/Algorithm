import sys 
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

homes = [] # 집 배열 선언
chickens = [] # 치킨집 배열 선언

for i in range(n):
  tmps = list(map(int, input().split()))
  for j in range(n):
    if tmps[j] == 1: # 집인 경우
      homes.append((i, j)) 
    if tmps[j] == 2: # 치킨집인 경우
      chickens.append((i, j)) 

result = int(1e9) # 최솟값을 찾기 때문에 무한대로 초기화

# 도시에 있는 치킨집 M개씩 조합
for chicken in combinations(chickens, m):
  tmp = 0
  for home in homes:
    min_val = int(1e9) # 한 집(home)에서 걱 치킨집까지의 거리 중 최소(min_val)
    for i in chicken:
      distance = abs(i[0] - home[0]) + abs(i[1] - home[1]) # 한 집(home)에서 걱 치킨집까지의 거리
      min_val = min(min_val, distance) # 최소 거리 갱신
    tmp += min_val
  result = min(result, tmp) # 도시의 치킨 거리 최솟값 갱신

print(result)
