import sys 
input = sys.stdin.readline 

n = int(input())
guests = list(map(int, input().split())) # 기관차가 끌고 가던 객차에 타고 있는 손님의 수
cnt = int(input()) # 소형 기관차가 최대로 끌 수 있는 객차의 수

# 최대로 운송할 수 있는 손님 수 
# 연속적으로 이어진 객체를 끌게 한다. 

# dp에는 기관차 수와 객차 번호에 해당하는 인덱스에 최대 손님 수 저장
# dp[n][m] = 100, 기관차 n개를 써서 m번 번호 객차까지 최대 손님수가 100명
dp = [[0] * (n + 1) for _ in range(4)]
# total에는 1번 객차부터 n번까지 총 인원수가 들어있다.
total = [0]
for i in range(n):
  total.append(total[i] + guests[i])

for i in range(1, 4):
  for j in range(cnt, n + 1):
    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - cnt] + total[j] - total[j - cnt]) # 객차 하나 뺐을 때 DP 값 + 연속적으로 이어진 객체들의 총 인원수
    
print(dp[3][n])
