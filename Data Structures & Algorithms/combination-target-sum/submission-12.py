class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        cur = []

        def dfs(index, total):
            if total > target:
                return
            elif total == target:
                res.append(cur.copy())
                return
            
            if index == len(nums):
                return
            
            # take current and keep idx
            cur.append(nums[index])
            dfs(index, total + nums[index])

            # move past
            cur.pop()
            dfs(index+1, total)

            return
        
        dfs(0, 0)
        return res