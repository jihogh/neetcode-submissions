class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n

        cache = [[-1] * n for _ in range(m)]

        def dfs(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if r == ROWS - 1 and c == COLS - 1:
                return 1

            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = dfs(r+1,c) + dfs(r, c+1)
            return cache[r][c]
        
        return dfs(0,0)