class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compare = set()
        for i in nums: 
            if i not in compare: 
                compare.add(i)
            else: 
                return True
        
        return False
        