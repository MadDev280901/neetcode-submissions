class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        requiredNum = collections.defaultdict(int)
        for i, e in enumerate(nums):
            if target-e not in requiredNum:
                requiredNum[e] = i
            
            else: 
                return [requiredNum[target-e], i]

        return -1

        