class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row, col):            
            if (
                row < 0 or row >= ROWS
                or col < 0 or col >= COLS
                or grid[row][col] != "1"
            ):
                return

            grid[row][col] = "0"
            
            bfs(row+1, col)
            bfs(row-1, col)
            bfs(row, col+1)
            bfs(row, col-1)

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    res += 1
                    bfs(row, col)

        return res