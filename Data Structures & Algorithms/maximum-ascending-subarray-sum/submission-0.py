class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr, best = 0, -float('inf')
        prev = -float('inf')

        for i in range(0, len(nums)):
            if nums[i] > prev:
                curr+=nums[i]
                prev = nums[i]
                best = max(curr, best)
            
            else:
                curr = nums[i]
                prev = nums[i]
                best = max(curr, best)
        
        return best

        