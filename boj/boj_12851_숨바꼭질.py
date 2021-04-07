## 12851. 숨바꼭질
import heapq
n, k = map(int, input().split())

INF = int(1e9)
dp = [INF for _ in range(100001)]

q = []

heapq.heappush(q, (0, n))
ans = INF
cnt = 0
while q:
  sec, now = heapq.heappop(q)
  
  if sec > ans:
    break
    
  if now == k:
    if ans == INF:
      ans = sec
      cnt += 1
    elif ans == sec:
      cnt += 1
    else:
      break
  
  if now - 1 >= 0 and dp[now - 1] >= sec + 1:
    dp[now - 1] = sec + 1
    heapq.heappush(q, (sec + 1, now - 1))
  if now + 1 <= 100000 and dp[now + 1] >= sec + 1:
    dp[now + 1] = sec + 1
    heapq.heappush(q, (sec + 1, now + 1))
  if now * 2 <= 100000 and dp[now * 2] >= sec + 1:
    dp[now * 2] = sec + 1
    heapq.heappush(q, (sec + 1, now * 2))

print(ans)
print(cnt)
