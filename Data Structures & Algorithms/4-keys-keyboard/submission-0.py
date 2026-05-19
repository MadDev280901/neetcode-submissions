class Solution:
    def maxA(self, n: int) -> int:
        memo = {}

        def dp(k):
            # Base cases
            if k <= 3:
                return k

            if k in memo:
                return memo[k]

            # Option 1: press 'A'
            ans = dp(k - 1) + 1

            # Option 2:
            # build something at step j,
            # then Ctrl-A, Ctrl-C, and paste
            for j in range(1, k - 2):
                ans = max(ans, dp(j) * (k - j - 1))

            memo[k] = ans
            return ans

        return dp(n)