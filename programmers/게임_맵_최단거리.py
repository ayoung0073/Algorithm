from collections import deque
import heapq
def solution(maps):
    INF = int(1e9)
    dp = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dp[0][0] = 1
    
    q = [(1, 0, 0)]
    
    r = len(maps)
    c = len(maps[0])
    
    while q:
        dist, x, y = heapq.heappop(q)
        if x == r - 1 and y == c - 1:
            break
        
        if x < r - 1 and maps[x + 1][y]: # 아래로 이동
            if dp[x + 1][y] > dist + 1: 
                dp[x + 1][y] = dist + 1
                heapq.heappush(q, [dist + 1, x + 1, y])
        if y < c - 1 and maps[x][y + 1]: # 오른쪽으로 이동
            if dp[x][y + 1] > dist + 1:
                dp[x][y + 1] = dist + 1
                heapq.heappush(q, [dist + 1, x, y + 1])
        if x != 0 and maps[x - 1][y]: # 위로 이동
            if dp[x - 1][y] > dist + 1:
                dp[x - 1][y] = dist + 1
                heapq.heappush(q, [dist + 1, x - 1, y])
        if y != 0 and maps[x][y - 1]: # 왼쪽으로 이동
            if dp[x][y - 1] > dist + 1:
                dp[x][y - 1] = dist + 1
                heapq.heappush(q, [dist + 1, x, y - 1])
            
    if dp[r - 1][c - 1] == INF:
        return -1
    else:
        return dp[r - 1][c - 1]
