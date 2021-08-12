### DP.
n = int(input())
power = list(map(int, input().split()))
power.reverse() # LIS 알고리즘을 위해 역순

dp = [1] * n

for i in range(1, n):
  for j in range(i):
    if power[j] < power[i]:
      dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

### 이분 탐색.
from bisect import bisect_left
import sys 
input = sys.stdin.readline 

n = int(input())
fight = list(map(int, input().split()))
# 이분 탐색을 위해 배열을 뒤집는다. (오름차순으로 save 배열에 저장할 것)
fight.reverse()
## 열외해야 하는 병사의 수를 출력해야 한다.
save = [fight[0]]

# save에 최대한 작은 값을 넣어야 한다. 그래야 다른 수들이 많이 들어올 수 있다.
# 크다면 append
for i in fight[1:]:
  if save[-1] < i:
    save.append(i)
  else:
    idx = bisect_left(save, i)
    save[idx] = i

print(n - len(save))
