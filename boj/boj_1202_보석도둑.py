## 1202. 보석 도둑
import sys
import heapq
input = sys.stdin.readline

# 보석의 개수, 가방의 개수
n, k = map(int, input().split())

info = [] # 보석의 정보(무게, 가격)
for _ in range(n):
  info.append(list(map(int, input().split())))

max_weight = []
for _ in range(k):
  max_weight.append(int(input())) # 가방에 담을 수 있는 최대 무게 c

# 상덕이가 훔칠 수 있는 보석의 최대 가격 구하라
info.sort()
max_weight.sort()

heap = [] # 최대힙 만들자
result = 0

# 가방 개수만큼 반복하자
jew = 0
for weight in max_weight:
  while jew < n:
    if weight >= info[jew][0]:
      heapq.heappush(heap, (-1) * info[jew][1]) # 최대힙 만들기 위해 -1 곱함
      jew += 1
    else:
      break
        
  if heap:
    result += (-1) * heapq.heappop(heap)

print(result)
