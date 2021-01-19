# 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력

n = int(input())
coins = list(map(int, input().split()))

coins.sort()

target = 1
for coin in coins:
  # 만들 수 없는 금액 찾았을 때 반복 종료
  if target < coin:
    break
  target += coin

# 만들 수 없는 금액 출력
print(target)
