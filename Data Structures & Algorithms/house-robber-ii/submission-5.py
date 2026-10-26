class Solution:
    def rob(self, nums: List[int]) -> int:
        end = len(nums) - 1

        memo = {}

        if len(nums) <= 1:
            return nums[0] if nums else 0

        def dfs(i, firstRobbed):
            if i == end:
                if firstRobbed:
                    return 0
                else:
                    return nums[end]
            if i > end:
                return 0

            if (i, firstRobbed) in memo:
                return memo[(i, firstRobbed)]
            
            memo[(i, firstRobbed)] = max(nums[i] + dfs(i+2, firstRobbed), dfs(i+1, firstRobbed))
            return memo[(i, firstRobbed)]

        return max(dfs(0, True), dfs(1, False))