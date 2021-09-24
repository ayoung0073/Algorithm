## 12865. 평범한 배낭
import sys 
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)] 
# dp[i][j] => i번째에서 무게가 j인 가치 최댓값 저장 

for i in range(1, n + 1): # 물건 인덱스
  for j in range(1, k + 1): # 무게 
    if j < arr[i][0]: 
      # 현재 물건의 가치를 비교하지 않으므로 이전 i - 1 번째 그대로 저장 
      dp[i][j] = dp[i - 1][j]
    else:
      dp[i][j] = max(dp[i - 1][j - arr[i][0]] + arr[i][1], dp[i - 1][j])
      # 현재 물건(i번째)의 가치를 포함한 경우와, 포함하지 않은 경우의 가치 중 최댓값으로 갱신한다.
    
print(dp[n][k])
