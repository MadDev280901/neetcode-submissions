class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        s_to_t = [0]*26
        for char in s:
            s_to_t[ord(char)-ord('a')]+=1
        
        for char in t:
            if s_to_t[ord(char)-ord('a')] == 0:
                return False
            
            else:
                s_to_t[ord(char)-ord('a')]-=1
        
        return True

        