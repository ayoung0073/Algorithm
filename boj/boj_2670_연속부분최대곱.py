import sys  
input = sys.stdin.readline
n = int(input())
dp = []
for _ in range(n):
  dp.append(float(input()))
result = 0
for i in range(n):
  mul = 1
  for j in range(i, n):
    mul *= dp[j]
    dp[i] = max(mul, dp[i])
  result = max(result, dp[i])
print('%.3f'%(result))
# print(round(result, 3))
