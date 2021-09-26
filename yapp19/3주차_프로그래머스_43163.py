## 단어 변환
INF = int(1e9)
answer = INF

def solution(begin, target, words):
    visited = [False for i in range(len(words))]
    length = len(target)
    def dfs(now, cnt):
        global answer
        if now == target:
            answer = min(answer, cnt)
            return
        for i in range(length):
            for j in range(len(words)):
                if not visited[j] and now[0:i] + now[i+1:length] == words[j][0:i] + words[j][i+1:length]:
                    visited[j] = True
                    dfs(words[j], cnt + 1)
                    visited[j] = False

    dfs(begin, 0)
    return answer if answer != INF else 0
        
