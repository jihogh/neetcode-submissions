class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def solve(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = cost[i] + min(solve(i+1), solve(i+2))
            return memo[i]
        
        return min(solve(0), solve(1))