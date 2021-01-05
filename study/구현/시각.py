# 00:00:00 ~ N:59:59 까지
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성
import time

n = int(input())

# second, minute에서 3 -> 30~39, (0~5)3 (정해져 있음) # 33중복
# hour에서 3 나올 경우는 03, 13, 23
start = time.time()
# 모든 경우의 수 - 3이 안나올 경우의 수?
if n < 3:
  result = (n+1) * 60 * 60 - (n+1) * 45 * 45
elif n < 13:
  tmp = n
  result = (n+1) * 60 * 60 - tmp * 45 * 45
elif n < 23:
  tmp = n - 1
  result = (n+1) * 60 * 60 - tmp * 45 * 45
else:
  tmp = n - 2
  result = (n+1) * 60 * 60 - tmp * 45 * 45
me = time.time() - start
print(result)

h = int(input())
start = time.time()

count = 0
for i in range(h+1):
  for j in range(60):
    for k in range(60):
      if '3' in str(i) + str(j) + str(k):
        count += 1
ans = time.time() - start
print(count)

print(me, ans)
print(min(me, ans))
    
