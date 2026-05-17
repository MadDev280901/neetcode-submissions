class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_map_a = {}
        freq_map_b = {}
        for char in ransomNote: 
            if char not in freq_map_a:
                freq_map_a[char]=1
            else:
                freq_map_a[char]+=1

        for char in magazine: 
            if char not in freq_map_b:
                freq_map_b[char]=1
            else:
                freq_map_b[char]+=1

        
        for key, item in freq_map_a.items(): 
            if key not in freq_map_b:
                return False
            if item > freq_map_b[key]:
                return False
            
        return True 
        

        