class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        cur = []

        def dfs(index):
            if sum(cur) > target:
                return
            elif sum(cur) == target:
                res.append(cur.copy())
                return
            
            if index == len(nums):
                return
            
            # take current and keep idx
            cur.append(nums[index])
            dfs(index)

            # move past
            cur.pop()
            dfs(index+1)

            return
        
        dfs(0)
        return res