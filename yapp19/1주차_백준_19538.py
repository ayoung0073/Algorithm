import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[]]

for _ in range(n):
  graph.append(list(map(int, input().split()))[:-1])

input()
start = list(map(int, input().split()))

ans = [-1] * (n + 1)

for s in start:
    ans[s] = 0

# 믿는 주변인의 수를 저장하는 배열
trust = [0] * (n + 1)  

def solve():
    q = deque(start)
    while q:
      curr = q.popleft()
      for e in graph[curr]:
        trust[e] += 1
        # 아직 믿지 않았고, 주변인의 절반 이상이 루머를 믿는 경우
        if ans[e] == -1 and trust[e] >= (len(graph[e]) + 1) // 2:
            ans[e] = ans[curr] + 1
            q.append(e)

solve()

print(' '.join(str(minutes) for minutes in ans[1:]))
