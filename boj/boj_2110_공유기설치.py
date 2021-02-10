## 2110. 공유기 설치
import sys

input = sys.stdin.readline
n, c = map(int, input().split()) # 집, 공유기의 개수

home = [int(input()) for _ in range(n)]

home.sort()

# 첫집과 끝집
start = 0
end = home[-1]

result = 0
while start <= end:
  mid = (start + end) // 2 # gap
  val = home[0]
  install = 1
  
  for i in range(1, n):
    if home[i] >= val + mid:
      install += 1  
      val = home[i]
  if install >= c: # 거리 넓히자
    start = mid + 1
    result = mid
  else: # 거리 좁히자
    end = mid - 1

print(result)
