## 신입 사원
import sys 
input = sys.stdin.readline 

t = int(input())
for _ in range(t):
  n = int(input())
  score = []
  for _ in range(n):
    score.append(list(map(int, input().split())))

  ans = 1

  score.sort() 
  interview_score = score[0][1]
  for score_comp in score[1:]:
    if score_comp[1] < interview_score: # 더 높은 순위(합격 가능)
      interview_score = score_comp[1]
      ans += 1
  
  print(ans)
