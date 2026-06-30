class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for i, e in enumerate(strs):
            tup = [0 for i in range(26)]

            for char in e: 
                tup[ord(char) - ord('a')] += 1

            tup = tuple(tup)
            if tup not in groups:
                groups[tup] = [e]
            else: 
                groups[tup].append(e)

        
        return list(groups.values())

            
        