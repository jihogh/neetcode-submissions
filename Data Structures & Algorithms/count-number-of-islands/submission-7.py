class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1':
                return
            
            grid[r][c] = '0'

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

            return

        numIslands = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    numIslands += 1
                    dfs(r,c)

        return numIslands