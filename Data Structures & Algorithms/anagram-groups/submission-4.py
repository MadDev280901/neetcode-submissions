class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramCollection = collections.defaultdict(list)
        for word in strs:
            repr = [0 for i in range(26)]
            for ch in word:
                repr[ord(ch)-ord('a')] += 1
            
            anagramCollection[tuple(repr)].append(word)
        
        return list(anagramCollection.values())

        