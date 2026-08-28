class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = -float('inf')
        lookupWindow = set()

        for r in range(len(s)):
            if s[r] not in lookupWindow:
                lookupWindow.add(s[r])
                maxLen = max(maxLen, r-l+1)

            else:
                while s[r] in lookupWindow:
                    lookupWindow.remove(s[l])
                    l+=1

                lookupWindow.add(s[r])
                
                

        return maxLen if maxLen != -float('inf') else 0 


            
        