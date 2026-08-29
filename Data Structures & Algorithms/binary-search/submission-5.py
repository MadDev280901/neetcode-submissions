import bisect 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target, hi = len(nums)-1)
        print(idx)
        return idx if nums[idx] == target else -1
        