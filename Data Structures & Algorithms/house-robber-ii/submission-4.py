class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def rob_simple(nums, start, end):
            memo = collections.defaultdict(int)

            def f(i):
                if i >= end:
                    return 0
                if i in memo:
                    return memo[i]
                
                else:
                    memo[i] = max(nums[i]+f(i+2), f(i+1))
                    return memo[i]
            
            return f(start)
        
        if n <= 1:
           return max(nums) 
        return max(rob_simple(nums, 0, n-1), rob_simple(nums, 1, n))
        
        
        