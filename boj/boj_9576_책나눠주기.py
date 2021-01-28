t = int(input())

for _ in range(t):
  result = 0
  n, m = map(int, input().split())
  books = [False] * (n + 1)
  reqs = []
  for _ in range(m):
    reqs.append(list(map(int, input().split())))

  reqs.sort(key = lambda x:x[1]) # b를 기준으로 오름차순
  
  while reqs:
    a, b = reqs.pop(0)
    for i in range(a, b + 1):
      if not books[i]: # False이면, 나눠줄 수 있음
        result += 1
        books[i] = True
        break
  print(result)
