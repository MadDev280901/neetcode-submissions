class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        dp = [0]*(n+1)
        dp[1] = 1

        for j in range(2, n+1):
            dp[j] = j%2 + dp[j//2]

        return dp
        