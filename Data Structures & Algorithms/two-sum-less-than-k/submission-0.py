from typing import List

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1
        best = -1

        while l < r:
            s = nums[l] + nums[r]

            if s < k:
                best = max(best, s)
                l += 1
            else:
                r -= 1

        return best