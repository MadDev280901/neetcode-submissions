class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        freq = {i:0 for i in s}
        for i in s:
            freq[i]+=1

        for i in s:
            freq[i]%=2
        
        return True if sum(freq.values()) <= 1 else False
        
        

        