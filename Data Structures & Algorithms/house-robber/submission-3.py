class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = collections.defaultdict(int)

        def f(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            else:
                memo[i] = max(nums[i]+f(i+2), f(i+1))
                return memo[i]
        
        return f(0)
        