class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def isAnagram(s1, s2):
            if len(s1) != len(s2):
                return False
            
            count = {}
            
            for char in s1:
                count[char] = count.get(char, 0) + 1
            for char in s2:
                if char not in count:
                    return False
                count[char] -= 1
                if count[char] < 0:
                    return False
                    
            return True

        groups = []
        for s in strs:
            if len(groups) > 0: 
                added = False
                for group in groups:
                    rep = group[-1]
                    if isAnagram(rep, s):
                        group.append(s)
                        added = True
                if not added:
                    groups.append([s])

            else:
                groups.append([s])

        return groups
        