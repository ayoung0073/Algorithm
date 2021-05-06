## 개미 전사

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, n) : # 항상 최댓값 저장하도록 하자
  dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])

print(dp)
print(dp[n - 1])
