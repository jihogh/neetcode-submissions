class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n + 1)

        def solve(n):
            if n == 0 or n == 1:
                return 1
            
            if memo[n] != -1:
                return memo[n]
            
            memo[n] = solve(n-1) + solve(n-2)
            return memo[n]

        return solve(n)