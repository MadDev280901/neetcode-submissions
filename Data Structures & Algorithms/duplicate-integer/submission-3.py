class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenSoFar = set()
        for num in nums: 
            if num in seenSoFar:
                return True

            seenSoFar.add(num)
        
        return False 