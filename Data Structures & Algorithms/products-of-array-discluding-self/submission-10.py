class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)

        counter = 1
        for i in range(0, len(nums)):
            pre[i] = counter
            counter *= nums[i]

        counter = 1
        for i in range(len(nums)-1,-1,-1):
            post[i] = counter
            counter *= nums[i]
        
        res = [0] * len(nums)
        for i in range(0, len(nums)):
            res[i] = pre[i] * post[i]

        return res