# 58984KB	388ms
import sys
import heapq

input = sys.stdin.readline 

arr = []
n = int(input())
for _ in range(n):
  s, t = map(int, input().split())
  arr.append((s, t))

arr.sort()

q = []

for i in arr:
  if not q:
    heapq.heappush(q, i[1])
  elif i[0] >= q[0]: # 강의실 새로 배정 안해도 되는 경우 
    heapq.heappop(q)
    heapq.heappush(q, i[1])
  else: # 새로 배정하는 경우
    heapq.heappush(q, i[1])
  
print(len(q))
    

### 시간 초과 케이스
# import sys

# input = sys.stdin.readline
# n = int(input())
# lessons = []
# for _ in range(n):
#   s, t = map(int, input().split())
#   lessons.append((s, t))

# lessons.sort(key = lambda x : x[0])

# arr = [0] # 끝나는 시간 배열
# for lesson in lessons:
#   s, t = lesson
#   if min(arr) <= s: # 시작 시간이 겹치지 않는 경우
#       arr.remove(min(arr))
#   arr.append(t)
#   print(s, t, arr)

# print(len(arr))
