class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        end = len(cost)
        memo = [-1] * end

        def dfs(i):
            # dfs(i) is the minimum cost to get to step n from step i
            if i >= end - 2: # if we're at the second to last or last step just pay and step up
                return cost[i]

            if memo[i] != -1:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]

        return min(dfs(0), dfs(1))