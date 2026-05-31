class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            t = nums[m]

            if t == target:
                return m 
            elif t > target:
                r = m-1
            else:
                l = m+1

        return l
        