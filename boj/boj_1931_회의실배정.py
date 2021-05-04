import heapq

n = int(input())
arr = []
for _ in range(n):
  s,e = map(int, input().split())
  arr.append([s, e])

arr.sort(key = lambda x:(x[1], x[0])) # 끝나는 시간 기준으로 오름차순 정렬
save = [0]
ans = 0
for i in range(len(arr)):
  start, end = arr[i]
  comp_end = heapq.heappop(save) # 끝나는 시간과 비교해야 함.
  if start >= comp_end:
    ans += 1
    heapq.heappush(save, end)
  else:
    heapq.heappush(save, comp_end)

print(ans)
