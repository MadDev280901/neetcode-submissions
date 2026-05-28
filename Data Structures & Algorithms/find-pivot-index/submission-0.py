class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]*len(nums)
        suffixSum = [0]*len(nums)
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            suffixSum[j] = suffixSum[j+1] + nums[j+1]
        
        for k in range(len(nums)):
            if prefixSum[k] == suffixSum[k]:
                return k
        
        return -1