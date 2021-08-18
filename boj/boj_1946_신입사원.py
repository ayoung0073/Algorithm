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
  # 순위 오름차순 정렬
  score.sort(key=lambda x:x[0]) 
  max_interview_score = score[0][1]
  for arr in score[1:]:
    if arr[1] < max_interview_score: # 더 높은 순위(합격 가능)
      max_interview_score = arr[1]
      ans += 1
  
  print(ans)


