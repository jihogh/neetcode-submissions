class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [-1] * len(cost)
        def calculate_cost(i):
            if i >= len(cost):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            memo[i] = cost[i] + min(calculate_cost(i+1), calculate_cost(i+2))
            return memo[i]
        
        return min(calculate_cost(0), calculate_cost(1))