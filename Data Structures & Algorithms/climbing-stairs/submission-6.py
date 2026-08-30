class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def f(i):
            if i >= (n-1):
                return 1
            if i in memo:
                return memo[i]
            
            else:
                memo[i] = f(i+1) + f(i+2)
                return memo[i]
        
        return f(0)
        