class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [0] * (len(cost) + 1)

        for i in range(2, len(cost)+1):
            two_back = memo[i-2] + cost[i-2]
            one_back = memo[i-1] + cost[i-1]

            memo[i] = min(two_back, one_back)
        
        return memo[len(cost)]