class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def f(i, j):
            if i < 0 or j < 0:
                return False
            if i > 0 and j == 0:
                return False
            if i == 0:
                return True
            
            else: 
                if s[i-1] == t[j-1]:
                    return f(i-1, j-1)
                else: 
                    return f(i, j-1)
        
        return f(len(s), len(t))
            
            
        