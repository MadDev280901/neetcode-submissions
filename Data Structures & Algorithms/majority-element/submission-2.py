class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] == majority:
                streak+=1
            
            else:
                if streak > 0:
                    streak-=1
                
                else: 
                    majority = nums[i]
                    streak = 1
        
        return majority 
                
        