class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqMapS = dict()
        for char in s:
            if char in freqMapS:
                freqMapS[char] += 1
            else: 
                freqMapS[char] = 1
        
        for char in t:
            if char not in freqMapS:
                return False 
            
            else: 
                if freqMapS[char] == 0:
                    return False 
                
                freqMapS[char]-=1
        
        return True if sum(freqMapS.values()) == 0 else False
        