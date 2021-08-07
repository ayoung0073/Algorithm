## 5557. 1학년

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n + 1)]

dp[0][arr[0]] = 1
for i in range(1, n - 1):
  for j in range(0, 21):
    if dp[i - 1][j] != 0:
      if j + arr[i] <= 20:
        dp[i][j + arr[i]] += dp[i - 1][j]
      if j - arr[i] >= 0:
        dp[i][j - arr[i]] += dp[i - 1][j]

print(dp[n - 2][arr[-1]])


### 0808 복습
## 1학년
'''
11
8 3 2 4 8 7 2 4 0 8 8
'''

import sys
inpuy = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n + 1)] # 0부터 20이하의 수가 index, 개수가 value

# + 또는 - 를 넣어야 한다.
dp[0][nums[0]] = 1 # dp[자릿수(인덱스))][해당값(만든 숫자)] = 경우의 수(해당 자릿수까지 계산하여 숫자가 만들어질 수 있는 경우의 수)
# dp[0][nums[0]] => 처음에 8은 0번째 자릿수(인덱스)라고 치고, 계산없이 8이 들어간다. 즉 0번째 자릿수에서 8이 될 수 있는 경우의 수 1가지 
for i in range(1, n - 1): # 우리가 목표하는 값 nums[n - 1] 전까지 계산한다.
# i 번째 자릿수(인덱스)를 계산한다.
  for j in range(21): # 숫자를 만들 수 있는지 확인하는 0 ~ 20의 숫자 (인덱스가 아니라 만들 숫자를 위한 값이다.)
    if j + nums[i] <= 20: # + 가능한 값일 때
      dp[i][j + nums[i]] += dp[i - 1][j] # (i - 1)번째 dp에서 숫자가 j인 경우의 수를 더한다. 
    if j - nums[i] >= 0: # - 가능한 값일 때 
      dp[i][j - nums[i]] += dp[i - 1][j]  # (i - 1)번째 dp에서 숫자가 j인 경우의 수를 더한다. 

print(dp[n - 2][nums[n - 1]])
