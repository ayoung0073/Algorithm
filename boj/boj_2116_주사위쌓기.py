import sys
input = sys.stdin.readline

n = int(input())
dice = []
for _ in range(n):
  dice.append(list(map(int, input().split())))

# a, f / b, d / c, e
dic = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

ans = 0
for idx in range(6):
  val = dice[0][idx]
  sum_val = 0
  for arr in dice:
    i = arr.index(val)
    j = dic[i]
    val = arr[j]
    if i > j:
      i, j = j, i
    sum_val += max(arr[0: i] + arr[i + 1: j] + arr[j + 1: 6])
  ans = max(ans, sum_val)

print(ans)
