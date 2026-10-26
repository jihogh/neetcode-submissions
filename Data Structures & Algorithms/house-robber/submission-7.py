class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            # rob this and skip next OR go to next (max of those two)
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]

        return dfs(0)