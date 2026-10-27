class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        length = len(nums)

        res = []

        for i in range(0, length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i+1, length - 1

            while l < r:
                numi, numl, numr = nums[i], nums[l], nums[r]

                if numi + numl + numr == 0:
                    res.append([numi, numl, numr])
                    
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif numi + numl + numr < 0:
                    l += 1
                else:
                    r -= 1
            
        return res