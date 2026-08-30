import collections

class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        memo = collections.defaultdict(int)
        MOD = 10**9 + 7
        
        def f(i):
            if i == 0:
                return 1
            if i in memo:
                return memo[i]
            
            ways = 0
            for k in range(0, i, 2):
                l = f(k)
                r = f(i - 2 - k)
                ways = (ways + l * r) % MOD
                
            memo[i] = ways
            return memo[i]
            
        return f(numPeople)