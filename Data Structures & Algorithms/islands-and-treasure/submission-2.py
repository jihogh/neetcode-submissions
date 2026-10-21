class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        chests = []

        ROWS, COLS = len(grid), len(grid[0])

        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    chests.append((r,c))

        queue = deque(chests)

        while queue:
            r, c = queue.popleft()

            for cr, cc in directions:
                nr, nc = r+cr, c+cc

                if not (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append([nr,nc])