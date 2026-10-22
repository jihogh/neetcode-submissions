class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []

        def dfs(index):
            if index == len(nums):
                res.append(cur.copy())
                return
            
            # take it
            cur.append(nums[index])
            dfs(index + 1)

            # remove
            cur.pop()
            dfs(index + 1)

            return
        
        dfs(0)
        return res