class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for word in strs:
            code = [0]*26 
            for char in word:
                code[ord(char)-ord('a')] += 1
            
            groups[tuple(code)].append(word)
        
        return list(groups.values())