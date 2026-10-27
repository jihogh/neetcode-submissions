class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0

        jumps = 0

        while r < len(nums) - 1:
            farthest = 0

            for num in range(l,r+1):
                farthest = max(farthest, num+nums[num])

            l, r = r+1, farthest
            jumps += 1
        
        return jumps