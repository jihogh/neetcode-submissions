class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        cur = []

        def dfs(index):
            if index == len(nums):
                res.append(cur.copy())
                return

            # take current number, move on
            cur.append(nums[index])
            dfs(index+1)

            cur.pop()         
            # don't take current number, skip all dupes
            while index + 1 < len(nums) and nums[index] == nums[index+1]:
                index += 1
            
            dfs(index+1)
        
        dfs(0)
        return res