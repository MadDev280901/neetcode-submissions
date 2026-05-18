class Solution:
    def numWays(self, n: int, k: int) -> int:

        memo = {}

        def f(n):

            if n == 1:
                return k

            if n == 2:
                return k * k

            if n in memo:
                return memo[n]

            memo[n] = (k - 1) * (f(n - 1) + f(n - 2))

            return memo[n]

        return f(n)