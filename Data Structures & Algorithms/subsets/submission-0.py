class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def help(start, ans):
            if start == len(nums):
                res.append(ans[:])
            else:
                ans.append(nums[start])
                help(start+1, ans)
                ans.pop()
                help(start+1, ans)
        
        help(0, [])
        return res
        