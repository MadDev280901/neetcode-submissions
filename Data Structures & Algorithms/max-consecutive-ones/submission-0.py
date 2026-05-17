class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currCnt, maxCnt = 0, -1
        for num in nums: 
            if num == 1: 
                currCnt += 1
                maxCnt = max(maxCnt, currCnt)
            
            else: 
                maxCnt = max(maxCnt, currCnt)
                currCnt = 0 
        
        return maxCnt 


        