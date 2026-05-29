class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        for u, v in zip(word1, word2):
            s+=u
            s+=v
        
        if len(word2) > len(word1):
            for i in range(len(word1), len(word2)):
                s+=word2[i]
        
        if len(word1) > len(word2):
            for j in range(len(word2), len(word1)):
                s+=word1[j]
        return s
        