class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        max_freq = 0
        
        for r in range(len(s)):
            # Add the current character to frequency map
            count[s[r]] = count.get(s[r], 0) + 1
            
            # Track the maximum frequency of any single character in the current window
            max_freq = max(max_freq, count[s[r]])
            
            # Check if the current window is invalid (requires more than k replacements)
            # Window length is (r - l + 1)
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            # Update our maximum length found so far
            res = max(res, r - l + 1)
            
        return res