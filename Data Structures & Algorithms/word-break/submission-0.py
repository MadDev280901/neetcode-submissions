class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = collections.defaultdict(bool)
        def f(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            ans = False
            for word in wordDict:
                l = len(word)
                if i + l - 1 < len(s) and s[i:i+l] == word:
                    ans = (ans or f(i+l))
                
            
            memo[i] = ans
            return memo[i]
        
        return f(0)
            