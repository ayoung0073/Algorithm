import sys
input = sys.stdin.readline

n, k = map(int, input().split())

order = list(map(int, input().split()))

max_arr = [0 for _ in range(k)]
for i in range(n):
  check = False
  for j in range(k):
    if order[i] > max_arr[j]:
      max_arr[j] = order[i]
      check = True
      break
  if not check:
    print("NO")
    exit(0)
print("YES")
