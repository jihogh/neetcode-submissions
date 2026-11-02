class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * n

        def dfs(i):
            if i > n:
                return 0
                
            if i == n:
                return 1

            if memo[i] != -1:
                return memo[i]

            memo[i] = dfs(i+1) + dfs(i+2)
            return memo[i]

        return dfs(0)