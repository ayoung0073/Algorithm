## 3980. 선발 명단

import sys
input = sys.stdin.readline 

def max_ability(player, cur_ability):
  global ans
  if player == 11:  # 모든 선수를 확인한 경우 
    if ans < cur_ability: # 답 갱신 조건 
      ans = cur_ability
    return 

  for i in range(11):
    if check[i]: continue # i번째 포지션을 확인하고 있는 경우 
    if arr[player][i]:
      check[i] = True # i번째 포지션에 대해 재귀 함수를 돌려보겠다. 
      max_ability(player + 1, cur_ability + arr[player][i])
      check[i] = False # 재귀 함수 호출 후 i번째 포지션 확인 끝

t = int(input()) # 테스트 케이스 수 

for _ in range(t):
  arr = []
  check = [False for _ in range(11)]
  ans = 0
  for _ in range(11):
    arr.append(list(map(int, input().split())))

  max_ability(0, 0) # 1번째 선수 능력 0부터 시작
  print(ans)
