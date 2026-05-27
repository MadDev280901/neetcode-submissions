class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l, r = 0, 0
        m, n = len(s), len(t)
        while l < m and r < n:
            if s[l] == t[r]:
                l+=1
                r+=1
            
            else:
                l+=1
        
        return n-r
        
        