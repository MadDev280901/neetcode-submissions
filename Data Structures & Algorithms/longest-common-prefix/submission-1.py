class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        lengths = list(map(lambda x : len(x), strings))

        ans = 0 
        for i in range(min(lengths)):
            ith_chars_set = set([string[i] for string in strings])

            if len(ith_chars_set) == 1:
                ans += 1
            
            else: 
                return strings[0][:ans]

        return strings[0][:ans] 
                

        