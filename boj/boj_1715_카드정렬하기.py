## 1715. 카드 정렬하기
import heapq

n = int(input())
cards = []
for _ in range(n):
  heapq.heappush(cards, int(input())) # heapq를 이용한 정렬

result = 0
while len(cards) >= 2:
  a = heapq.heappop(cards)
  b = heapq.heappop(cards)
  heapq.heappush(cards, a + b) 
  result += (a + b)

print(result)
