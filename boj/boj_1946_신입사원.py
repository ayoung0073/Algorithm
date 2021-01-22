## 1946. 신입 사원
import sys

input = sys.stdin.readline
t = int(input()) # 테스트 케이스의 개수

scores = [[] for i in range(t)]
for i in range(t):
  n = int(input()) # 지원자 수
  for j in range(n):
    a, b = map(int, input().split())
    scores[i].append((a, b))

  scores[i].sort(key = lambda x: x[0]) # 서류 심사 순위를 기준으로 오름차순 정렬

# 나보다 서류 성적 좋은 애들 중, 가장 순위가 높은 것보다 높으면 될 듯하다 max값 하나 지정하자

for i in range(t):
  max_score = len(scores[i]) + 1
  count = 0
  for score in scores[i]:
    if score[1] < max_score: # 더 높은 순위일 때 통과함
      count += 1
      max_score = min(max_score, score[1])
  print(count)
