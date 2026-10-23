class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        visiting = set()
        cur = []

        def dfs(r,c):
            if "".join(cur) == word:
                return True

            if not word.startswith("".join(cur)):
                return False

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visiting:
                return False
            
            cur.append(board[r][c])
            visiting.add((r,c))

            if dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1):
                return True

            visiting.remove((r,c))
            cur.pop()

            return
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c):
                    return True

        return False