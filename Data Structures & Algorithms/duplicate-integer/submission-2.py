class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSoFar = set()
        for num in nums: 
            if num not in seenSoFar:
                seenSoFar.add(num)
            
            else: 
                return True 
        
        return False 
        