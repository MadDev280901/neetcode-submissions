class Solution:
    def rob(self, nums: List[int]) -> int:
        # this is a version of maximum-weighted-independent-set 
        if len(nums)<=2: 
            return max(nums)
        else:
            a, b = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)): 
                a, b = b, max(a+nums[i], b)

            return b 


        