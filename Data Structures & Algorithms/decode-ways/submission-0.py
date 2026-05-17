class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        # dp[i] = number of ways to decode string of length i
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1 # One way to decode empty string (conceptually)
        dp[1] = 1 # One way to decode the first char (we already checked it's not '0')
        
        for i in range(2, n + 1):
            # 1. Check if single digit (s[i-1]) is valid
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # 2. Check if two digits (s[i-2:i]) are valid
            two_digit = int(s[i-2 : i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
                
        return dp[n]