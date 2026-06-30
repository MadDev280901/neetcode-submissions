class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, e in enumerate(nums): 
            if target-e not in seen:
                seen[e]= i 
            
            else: 
                return [seen[target-e], i]

        return []
        