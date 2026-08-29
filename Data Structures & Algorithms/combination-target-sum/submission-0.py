class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, target, ans):
            if target == 0:
                res.append(ans[:])
                return 
            
            if start >= len(nums) or target < 0:
                return 
            
            else: 
                ans.append(nums[start])
                backtrack(start, target - nums[start], ans)

                ans.pop()
                backtrack(start+1, target, ans)

                return 
        
        backtrack(0, target, [])
        return res
            
        