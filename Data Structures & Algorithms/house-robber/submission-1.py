class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            memo[i] = max(nums[i] + solve(i+2), solve(i+1))
            return memo[i]
        
        return solve(0)