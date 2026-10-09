class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def process(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return None
            else:
                grid[r][c] = 2
                rotten.appendleft((r,c))

        ROWS, COLS = len(grid), len(grid[0])

        elapsed = -1

        rotten = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
        
        while rotten:
            amtRotten = len(rotten)

            for i in range(amtRotten):
                r, c = rotten.pop()

                process(r+1, c)
                process(r-1, c)
                process(r, c+1)
                process(r, c-1)
            
            elapsed += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return max(0,elapsed)