class Solution:
    def numWays(self, n: int, k: int) -> int:
        def color(n, k, memo):
            if n == 0: 
                return 1
            if n == 1:
                return k
            if n == 2: 
                return k*k
            
            else:
                if n in memo:
                    return memo[n]

                memo[n] = (k-1)*(color(n-2, k, memo) + color(n-1, k, memo))
                return memo[n]

        return color(n, k, {})

                