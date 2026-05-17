class Solution:
    def climbStairsMemo(self, n:int, memo): 
        if n<=1: 
            return 1
        
        else: 
            if n in memo: 
                return memo[n]
            
            left = self.climbStairsMemo(n-1, memo)
            right = self.climbStairsMemo(n-2, memo)
            memo[n] = left + right 

            return memo[n]

    def climbStairs(self, n: int) -> int:

        return self.climbStairsMemo(n, {})