class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1:
            return nums[0]
        
        memo = [[-1] * 2 for i in range(len(nums))]

        # flag tells us later if first house was robbed or not
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            memo[i][flag] = max(dfs(i + 1, flag), nums[i] + dfs(i + 2, flag))
            return memo[i][flag]

        return max(dfs(0, True), dfs(1, False))