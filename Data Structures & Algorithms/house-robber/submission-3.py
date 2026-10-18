class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i):
            if i >= len(nums):
                return 0

            if memo[i] != -1:
                return memo[i]
            
            skip = dp(i+1)
            rob_current = nums[i] + dp(i+2)
            memo[i] = max(skip, rob_current)
            return memo[i]
        
        return dp(0)