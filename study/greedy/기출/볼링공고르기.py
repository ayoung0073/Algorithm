import sys
import time
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

arr = [0] * 11 # 1부터 10까지의 무게를 담을 수 있는 리스트

## 시간 복잡도 큼
start = time.time()
res = 0
for i in range(n - 1):
  for j in range(i + 1, n):
    if data[i] != data[j]:
      res += 1

print(res)
print(time.time() - start)


start = time.time()
for i in data:
  arr[i] += 1 # 각 무게에 해당하는 볼링의 개수 카운트

res = 0
for i in range(1, m + 1):
  # 1부터 m까지의 각 무게에 대한 처리
  n -= arr[i] # 무게가 i인 볼링의 개수(A가 선택할 수 있는 개수) 제외
  res += arr[i] * n # B가 선택하는 경우의 수와 곱하기

print(res)
print(time.time() - start)
