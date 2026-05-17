class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        lengths = list(map(lambda x : len(x), strings))

        ans = ""
        for i in range(min(lengths)):
            ith_chars_set = set([string[i] for string in strings])

            if len(ith_chars_set) == 1: 
                ans+=ith_chars_set.pop()
            
            else: 
                return ans 

        return ans 
                

        