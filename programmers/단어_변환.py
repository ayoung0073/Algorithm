from collections import deque
def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    q = deque()
    
    INF = int(1e9)
    length = len(begin)
    dp = [INF] * len(words)
    q.append((begin, 0, -1))
    
    while q:
        now, cnt, idx = q.popleft()
        if now == target:
            return cnt
        
        for i in range(length):
            if i == idx: continue
            if now[i] != target[i]:
                for word in words:
                    if word[0:i] + word[i+1:length] == now[0:i] + now[i+1:length] and dp[words.index(word)] > cnt + 1:  # index i 제외하고 다 비교하기
                        dp[words.index(word)] = cnt + 1
                        q.append((word, cnt + 1, i))
    
    return 0
