class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        to_place = nums[0]
        perms = self.permute(nums[1:])
        res = []

        for perm in perms:
            for i in range(len(perm)+1):
                copy = perm.copy()
                copy.insert(i, to_place)
                res.append(copy)
        
        return res