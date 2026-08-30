import collections

class Solution:
    def maxA(self, n: int) -> int:
        memo = collections.defaultdict(int)
        
        def f(x):
            if x <= 6:
                return x
            
            if x in memo:
                return memo[x]
          
            memo[x] = max((x - j - 1) * f(j) for j in range(1, x - 2))
            
            return memo[x]
            
        return f(n)