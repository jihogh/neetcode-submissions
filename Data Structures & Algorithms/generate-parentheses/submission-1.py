class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""

        def dfs(numOpen, numClose):
            nonlocal cur
            if numOpen == n and numClose == n:
                res.append(cur)
                return
            if numOpen > n or numClose > n:
                return
            
            if numClose < numOpen:
                cur += ")"
                dfs(numOpen, numClose+1)
                cur = cur[:-1]
            
            if numOpen < n:
                cur += "("
                dfs(numOpen+1, numClose)
                cur = cur[:-1]
            
        dfs(0,0)
        return res