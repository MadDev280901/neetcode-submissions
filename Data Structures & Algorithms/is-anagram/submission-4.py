class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
            
        freq_map = {i:0 for i in s}
        for i in s:
            freq_map[i]+=1
        
        for j in t:
            if j not in freq_map:
                return False
            
            if freq_map[j] == 0:
                return False
            
            freq_map[j] -= 1
        
        return True
        