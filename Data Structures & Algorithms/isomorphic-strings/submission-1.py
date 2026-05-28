class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        else:
            if s == t:
                return True

            isomap = {i:'' for i in s}
            l, r = 0, 0
            while l < len(s) and r < len(t):
                if isomap[s[l]] == '' and t[r] not in set(isomap.values()):
                    isomap[s[l]] = t[r]
                    l+=1
                    r+=1
                
                else: 
                    if isomap[s[l]]!=t[r]:
                        return False
                    
                    else:
                        l+=1
                        r+=1

            print(isomap)
            return True
                
        
    
        