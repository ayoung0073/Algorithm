import sys
import heapq

input = sys.stdin.readline
n = int(input())
lessons = []
for _ in range(n):
  s, t = map(int, input().split())
  lessons.append((s, t))

lessons.sort(key = lambda x : x[0])

arr = [] # 끝나는 시간 배열
for lesson in lessons:
  s, t = lesson
  if arr and arr[0] <= s: 
    # 끝나는 시간의 최솟값이 시작시간보다 빠른 경우, 
    # 최솟값을 갱신하기 때문에, 최솟값을 pop한 후
    # push
    heapq.heappop(arr)
  heapq.heappush(arr, t)
  print(s, t, arr)

print(len(arr))

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
