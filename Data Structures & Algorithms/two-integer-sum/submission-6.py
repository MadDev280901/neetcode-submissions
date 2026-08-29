class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matchPair = collections.defaultdict(int)
        for i, e in enumerate(nums):
            if target-e in matchPair:
                return [matchPair[target-e], i]
            
            else: 
                matchPair[e] = i 
        
        return []
        