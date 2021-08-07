# 10844. 쉬운 계단 수
# 길이가 N인 계단 수가 총 몇 개 있는지 구하는 문제

n = int(input())
# 현재 자릿 수까지의 경우의 수를 구해야 함.
# dp[자릿수][현재 값] = 총 개수
# 답 : sum(dp[n])

dp = [[0 for _ in range(10)] for _ in range(n + 1)]

# 첫 번째 자리수에는 0 제외하고 다 가능하다. 1로 초기화하자.
for i in range(1, 10):
  dp[1][i] = 1

# i는 자릿 수
for i in range(2, n + 1):
  # 0 은 이전 숫자가 없으니 따로 구한다.
  dp[i][0] += dp[i - 1][1]
  # 1 ~ 8
  for num in range(1, 9):
    dp[i][num] = dp[i - 1][num - 1] + dp[i - 1][num + 1]
  # 9는 다음 숫자가 없으니 따로 구한다.
  dp[i][9] += dp[i - 1][8]

print(sum(dp[n]) % 1_000_000_000)
