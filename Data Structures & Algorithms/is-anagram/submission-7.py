class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m1, m2 = [0]*26, [0]*26
        for char in s:
            m1[ord(char)-ord('a')] += 1
        for char in t:
            m2[ord(char)-ord('a')] += 1
        
        for i in range(26):
            if m1[i]!=m2[i]:
                return False

        return True
        