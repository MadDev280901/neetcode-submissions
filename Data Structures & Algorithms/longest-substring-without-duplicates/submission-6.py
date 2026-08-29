class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        w = set()

        maxLen = -float('inf')
        for r in range(len(s)):
            if s[r] not in w:
                w.add(s[r])
                maxLen = max(maxLen, r-l+1)
            
            else:
                while s[r] in w:
                    w.remove(s[l])
                    l+=1
                
                w.add(s[r])
                maxLen = max(maxLen, r-l+1)
            
        return max(maxLen, 0)
        