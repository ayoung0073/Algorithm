import sys
from heapq import *
input = sys.stdin.readline

n = int(input())
cards = []
for _ in range(n):
  heappush(cards, int(input()))

ans = 0
while len(cards) >= 2:
  a = heappop(cards)
  b = heappop(cards)
  heappush(cards, a + b)
  ans += a + b

print(ans)
