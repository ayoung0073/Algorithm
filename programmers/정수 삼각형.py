def solution(triangle):
    height = len(triangle)
    dp = [[0] * 500 for _ in range(500)]
    def dfs(h, idx):
        if h == height - 1:
            return triangle[h][idx]
        if dp[h][idx] != 0:
            return dp[h][idx]
        dp[h][idx] = triangle[h][idx] + max(dfs(h + 1, idx), dfs(h + 1, idx + 1))
        return dp[h][idx]
            
    return dfs(0, 0)
