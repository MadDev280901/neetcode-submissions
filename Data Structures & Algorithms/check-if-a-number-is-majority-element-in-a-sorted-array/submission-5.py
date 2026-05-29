from typing import List

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        
        # Find first occurrence of target (leftmost index)
        left, right = 0, n - 1
        first = n  # default if not found
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
                first = mid
            else:
                left = mid + 1
        
        # If first is out of bounds or not target, no majority
        if first >= n or nums[first] != target:
            return False
        
        # Check if element n/2 positions later is still target
        # i.e., target appears at least floor(n/2)+1 times
        return first + n // 2 < n and nums[first + n // 2] == target