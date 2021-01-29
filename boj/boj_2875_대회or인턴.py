## 2875_대회or인턴.py

#  최대 팀 수 구하기

n, m, k = list(map(int, input().split()))

if n >= 2 * m:
  result = m
  k -= n - 2 * m # 남은 여학생을 인턴십에 참여시키기
else:
  result = n // 2
  k -= m - n // 2 # 남은 남학생을 인턴십에 참여

if k > 0: # 인턴십에 참여해야하는 인원이 남아있는 경우
  if k % 3 == 0:
    result -= k // 3 
  else:
    result -= k // 3 + 1

print(result)
