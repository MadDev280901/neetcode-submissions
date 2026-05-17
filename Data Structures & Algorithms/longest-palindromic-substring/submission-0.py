class Solution:
    def is_palindrome(self, s): 
        n = len(s)
        l, r = 0, n-1
        while l < r: 
            if s[l] != s[r]:
                return False 
            l+=1
            r-=1
        return True 
    def longestPalindrome(self, s: str) -> str:
        # #brute-force
        # best, bestlen = "", -1 
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         if self.is_palindrome(s[i:j+1]): 
        #             curr_len = len(s[i:j+1])
        #             if curr_len > bestlen: 
        #                 bestlen = curr_len 
        #                 best = s[i:j+1]

        #         else: 
        #             continue 
        
        # return best 

        n = len(s)
        if n == 0:
            return ""

        # dp[i][j] = True if s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # Base case: single characters
        for i in range(n):
            dp[i][i] = True

        # Base case: length 2 substrings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Substrings of length >= 3
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        return s[start:start + max_len]

        