class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        def binary_search(l, r):
            print(l,r)
            while l <= r:
                m = l + (r-l) // 2

                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    return m

            return -1

        min_idx = 0

        while l <= r:
            if nums[l] < nums[r]:
                # found sorted part
                if nums[l] < nums[min_idx]:
                    min_idx = l
                break

            m = l + (r-l) // 2

            if nums[m] < nums[min_idx]:
                min_idx = m

            if nums[l] <= nums[m]:
                # then min must be on the right
                l = m + 1
            else:
                r = m - 1

        if min_idx == 0:
            return binary_search(0, len(nums)-1)
        if target >= nums[0]:
            return binary_search(0, min_idx-1)
        else:
            return binary_search(min_idx, len(nums)-1)