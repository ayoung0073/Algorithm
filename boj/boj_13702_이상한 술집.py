import sys
input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
for _ in range(n):
  arr.append(int(input()))

end = sum(arr) // k
start = 0
res = 0
while True:
  mid = (start + end) // 2
  cnt = 0
  for i in arr:
    cnt += i // mid
  if cnt < k:
    end = mid - 1
  else:
    start = mid + 1
    if mid == res: # 조건!
      print(res)
      break
    res = mid
