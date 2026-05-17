class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        if m > n: 
            return False 
        else: 
            l, r = 0, 0
            while l < m and r < n: 
                if s[l] != t[r]:
                    r+=1
                else:
                    l+=1
                    r+=1
            
            return l == m


        