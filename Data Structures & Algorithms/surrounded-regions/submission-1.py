class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c,target,change):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or not board[r][c] == target:
                return
            
            board[r][c] = change

            dfs(r+1,c,target,change)
            dfs(r-1,c,target,change)
            dfs(r,c-1,target,change)
            dfs(r,c+1,target,change)
        
            return
        
        for r in range(ROWS):
            dfs(r,0,'O','#')
            dfs(r,COLS-1,'O','#')
        
        for c in range(COLS):
            dfs(0,c,'O','#')
            dfs(ROWS-1,c,'O','#')
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'

        return