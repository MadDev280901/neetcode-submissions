class Solution:
    def rob(self, nums: List[int]) -> int:
        def robMemo(i, nums, memo): 
            if i == 0: 
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            else: 
                if i in memo: 
                    return memo[i] 

                left = nums[i] + robMemo(i-2, nums, memo)
                right = robMemo(i-1, nums, memo)
                
                memo[i] = max(left, right)
                return memo[i]

        return robMemo(len(nums)-1, nums, {})

        