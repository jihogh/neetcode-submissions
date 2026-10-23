class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = ""

        def dfs(num_open, num_close):
            nonlocal cur
            if num_open + num_close == 2 * n:
                res.append(cur)
                return
            
            if num_open > num_close:
                cur += ")"
                dfs(num_open, num_close+1)
                cur = cur[:-1]

            if num_open < n:
                cur += "("
                dfs(num_open+1, num_close)
                cur = cur[:-1]
            
            return
        
        dfs(0,0)
        return res