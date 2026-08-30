class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = collections.defaultdict(int)
        def isPossible(i, lSum, rSum):
            if i == len(nums) and lSum==rSum:
                return True
            if i == len(nums) and lSum!=rSum:
                return False
            
            if (i, lSum, rSum) in memo:
                return memo[(i, lSum, rSum)]
            
            memo[(i, lSum, rSum)] = (isPossible(i+1, lSum+nums[i], rSum) or isPossible(i+1, lSum, rSum+nums[i]))
            return memo[(i, lSum, rSum)]
        return isPossible(0, 0, 0)