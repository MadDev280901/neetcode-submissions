class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        lprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
        
        rprod = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= rprod
            rprod *= nums[i]
        
        return res
        