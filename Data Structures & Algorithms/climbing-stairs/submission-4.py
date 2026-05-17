class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 2: 
        #     return n 
        # else: 
        #     ans = self.climbStairs(n-1)+self.climbStairs(n-2)
        #     return ans
        if n<=2: 
            return n 
        else: 
            a, b = 1, 2
            for i in range(2, n):
                a, b = b, a+b 
            
            return b
        