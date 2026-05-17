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
        if not s:
            return ""

        # Transform string
        T = "#" + "#".join(s) + "#"
        n = len(T)
        P = [0] * n

        C = 0
        R = 0

        for i in range(n):
            mirror = 2 * C - i

            if i < R:
                P[i] = min(P[mirror], R - i)

            # Expand around center i
            a = i + P[i] + 1
            b = i - P[i] - 1
            while a < n and b >= 0 and T[a] == T[b]:
                P[i] += 1
                a += 1
                b -= 1

            # Update center and right boundary
            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Find max palindrome
        max_len = max(P)
        center = P.index(max_len)

        start = (center - max_len) // 2
        return s[start:start + max_len]
