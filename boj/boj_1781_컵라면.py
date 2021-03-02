import heapq
import sys
input = sys.stdin.readline

n = int(input())
prob = []
for _ in range(n):
    a, b = map(int, input().split())
    prob.append((a, b))

prob.sort()

q = []

for i in prob:
    heapq.heappush(q, i[1])
    if i[0] < len(q):
        heapq.heappop(q)
    
print(sum(q))
