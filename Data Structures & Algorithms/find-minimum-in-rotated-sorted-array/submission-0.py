class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + (r - l) // 2
            
            if nums[m] > nums[r]:
                # Minimum is in the right half
                l = m + 1
            else:
                # Minimum is in the left half (including m)
                r = m
                
        return nums[l]