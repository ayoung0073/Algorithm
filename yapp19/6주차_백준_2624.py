## 2624 동전 바꿔주기

import sys 
input = sys.stdin.readline

t = int(input()) # 지폐 금액
k = int(input()) # 동전 가지 수

total_count = 0
# 동전의 금액 p, 동전 개수 n
coins = []
for _ in range(k):
  p, n = map(int, input().split())
  coins.append((p, n))
  total_count += n

dp = [[-1] * k for _ in range(t)]

# 현재 금액과 동전 index
def cal(cur_val, index):
  if cur_val == t:
    return 1
  elif index == k: # 동전 끝
    return 0
  if dp[cur_val][index] != -1: # 이미 계산된 경우는 바로 반환한다.
    return dp[cur_val][index]
  
  dp[cur_val][index] = 0 # 계산 진행했다는 표시.

  # 해당 index의 동전을 하나씩 늘려본다.
  for i in range(coins[index][1] + 1):
    if cur_val + coins[index][0] * i > t:
      # 목표 금액보다 크다면 반복문 종료한다.
      break
    # 해당 index의 동전 개수를 계산한 금액과 함께 다음 index 의 동전 계산한다.
    dp[cur_val][index] += cal(cur_val + coins[index][0] * i, index + 1)
  return dp[cur_val][index]

# 내림차순 정렬하는 경우 제일 빠른데,, 왜지?
# coins.sort(reverse=True)
print(cal(0, 0))
