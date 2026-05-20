class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        memo = {}

        # returns True iff s[i:j+1] is a palindrome
        def is_pal(i, j):

            # empty or single-char substring
            if i >= j:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = (
                s[i] == s[j]
                and
                is_pal(i + 1, j - 1)
            )

            return memo[(i, j)]

        best_l = 0
        best_r = 0

        # try every substring
        for i in range(n):
            for j in range(i, n):

                if is_pal(i, j):

                    if (j - i) > (best_r - best_l):
                        best_l = i
                        best_r = j

        return s[best_l:best_r + 1]