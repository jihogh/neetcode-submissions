class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            if memo[i] != -1:
                return memo[i]

            res = dfs(i+1)
            
            if len(s) - i >= 2 and 10 <= int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            
            memo[i] = res
            return res

        return dfs(0)