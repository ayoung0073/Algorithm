import sys  
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
q = []
heapq.heappush(q, (0, n))
INF = int(1e9)
dp = [INF for _ in range(100001)]
min_cnt = INF
answer_cnt = 0

while q: 
  cnt, n = heapq.heappop(q)

  if n == k:
    if min_cnt == INF:
      min_cnt = cnt
      answer_cnt = 1
    elif cnt == min_cnt:
      answer_cnt += 1
    else:
      break

  if n - 1 >= 0 and dp[n - 1] >= cnt + 1:
    dp[n - 1] = cnt + 1
    heapq.heappush(q, (cnt + 1, n - 1))

  if n + 1 <= 100000 and dp[n + 1] >= cnt + 1:
    dp[n + 1] = cnt + 1
    heapq.heappush(q, (cnt + 1, n + 1))

  if n * 2 <= 100000 and dp[n * 2] >= cnt + 1:
    dp[n * 2] = cnt + 1
    heapq.heappush(q, (cnt + 1, n * 2))

print(min_cnt)
print(answer_cnt)
