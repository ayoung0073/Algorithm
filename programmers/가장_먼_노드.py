from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    visited[1] = True
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    
    arr = [0] * (n + 1)
    q = deque([(0, 1)])
    while q:
        cnt, now = q.popleft()
        arr[now] = cnt
        for i in graph[now]:
            if not visited[i]:
                q.append((cnt + 1, i))
                visited[i] = True
                
    return arr.count(max(arr))
