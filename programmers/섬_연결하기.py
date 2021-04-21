def solution(n, costs):
    answer = 0
    # cost 기준으로 정렬
    costs.sort(key = lambda x : x[2])
    
    parent = [0] * n
    
    for i in range(len(parent)):
        parent[i] = i # 부모 노드 자기 자신으로 초기화
    
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
            
    for a, b, cost in costs:
        a, b = min(a, b), max(a, b)
        if find_parent(parent, a) != find_parent(parent, b):
            answer += cost
            union_parent(parent, a, b)
    
    return answer
