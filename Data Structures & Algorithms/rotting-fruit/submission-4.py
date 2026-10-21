class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isValid(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or not grid[r][c] == 1:
                return False
            return True

        rotten = []

        ROWS, COLS = len(grid), len(grid[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        num_fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                elif grid[r][c] == 1:
                    num_fresh += 1

        queue = deque(rotten)

        minutes_passed = 0

        while queue and num_fresh > 0:
            amountToProcess = len(queue)

            for i in range(amountToProcess):
                r,c = queue.popleft()

                for dr,dc in directions:
                    if isValid(r+dr,c+dc):
                        queue.append((r+dr,c+dc))
                        grid[r+dr][c+dc] = 2
                        num_fresh -= 1
            
            minutes_passed += 1

        return minutes_passed if num_fresh == 0 else -1