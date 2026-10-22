class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacific, atlantic = set(), set()

        res = []

        def find_pacific(r,c,prevh):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevh or (r,c) in pacific:
                return
            
            pacific.add((r,c))

            find_pacific(r+1,c,heights[r][c])
            find_pacific(r-1,c,heights[r][c])
            find_pacific(r,c+1,heights[r][c])
            find_pacific(r,c-1,heights[r][c])
        
        def find_atlantic(r,c,prevh):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in atlantic or heights[r][c] < prevh:
                return
            
            atlantic.add((r,c))

            find_atlantic(r-1,c,heights[r][c])
            find_atlantic(r+1,c,heights[r][c])
            find_atlantic(r,c-1,heights[r][c])
            find_atlantic(r,c+1,heights[r][c])

        for r in range(ROWS):
            find_pacific(r,0,float("-inf"))
            find_atlantic(r,COLS-1,float("-inf"))
        
        for c in range(COLS):
            find_pacific(0,c,float("-inf"))
            find_atlantic(ROWS-1,c,float("-inf"))

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res