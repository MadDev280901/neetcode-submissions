class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict()
        for char in s: 
            if char not in freq: 
                freq[char] = 1
            else: 
                freq[char] += 1

        for i, f in freq.items(): 
            if f==1: 
                return s.index(i)
        
        return -1
        