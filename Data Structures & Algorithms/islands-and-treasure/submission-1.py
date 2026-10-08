class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def processCell(r,c,dist):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != 2147483647:
                return None
            
            grid[r][c] = dist
            return [r,c]
        
        treasures = deque()
        dist = 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    treasures.append([r,c])

        while treasures:
            numLevel = len(treasures)

            for i in range(numLevel):
                r, c = treasures.pop()

                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    neighbor = processCell(nr, nc, dist)
                    if neighbor is not None:
                        treasures.appendleft(neighbor)

            dist += 1
