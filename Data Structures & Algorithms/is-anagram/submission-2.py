class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
            
        lookup = [0]*26
        for char in s: 
            lookup[ord(char)-ord('a')]+=1
        
        for char in t: 
            if lookup[ord(char)-ord('a')] <= 0: 
                return False 
            lookup[ord(char)-ord('a')] -=1

        return True

        
        