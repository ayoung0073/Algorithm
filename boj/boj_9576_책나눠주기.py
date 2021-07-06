import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  books = [False] * (n + 1)
  requests = []
  for _ in range(m):
    a, b = map(int, input().split())
    requests.append((a, b))

  requests.sort(key=lambda x:x[1]) # b번을 기준으로 오름차순

  cnt = 0
  # 앞에서부터 search하여 값이 False이면 나눠준다.
  for a, b in requests:
    for i in range(a, b + 1):
      if not books[i]:
        books[i] = True
        cnt += 1
        break
  print(cnt)
