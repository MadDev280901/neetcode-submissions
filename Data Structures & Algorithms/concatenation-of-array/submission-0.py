class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*(2*len(nums))

        for i, e in enumerate(nums): 
            ans[i], ans[len(nums)+i] = e, e
    
        return ans
        