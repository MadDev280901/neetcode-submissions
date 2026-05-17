class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, num in enumerate(nums): 
            if target-num in seen.keys(): 
                return [seen[target-num], i]
            else: 
                seen[num] = i 
        
        return False 
        