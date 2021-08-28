## 2110 공유기 설치
import sys 
input = sys.stdin.readline

n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort()

install = 0

left = 0
right = homes[-1] - homes[0]

ans = 0

while left <= right:
  mid = (left + right) // 2
  cnt = 1
  before = homes[0]

  for home in homes[1:]:
    if home >= before + mid:
      cnt += 1
      before = home
  
  if cnt >= c:
    ans = max(mid, ans)
    left = mid + 1
  else:
    right = mid - 1

print(ans)
