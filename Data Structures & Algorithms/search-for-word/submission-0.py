class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == None or word[i] != board[r][c]:
                return False
            
            board[r][c] = None
            res = (dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1))
            board[r][c] = word[i]
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0) == True:
                    return True
        
        return False