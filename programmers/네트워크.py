import sys
input = sys.stdin.readline

def solution(n, computers):
    def find_parent(parent, x):
        while parent[x] != x:
            x = parent[x]
            
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    parent = [0] * n
    
    for i in range(n):
        parent[i] = i
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union_parent(parent, i, j)
        
    answer = n
    for i in range(n):
        if parent[i] != i:
            answer -= 1
            
    return answer
