class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        # nums = list(map(lambda x : x%2 , nums))
        for i in range(1, len(nums)):
            if (nums[i] + nums[i-1])%2 == 0:
                return False
        
        return True
        