class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict(int)

        for i, e in enumerate(nums): 
            if target-e not in lookup: 
                lookup[e] = i
            
            else: 
                return [lookup[target-e], i]
        print(lookup)
        return False 

        