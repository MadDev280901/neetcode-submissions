class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt, maxcnt = 0, -1
        for num in nums: 
            if num == 1: 
                cnt+=1
            else: 
                maxcnt = max(maxcnt, cnt)
                cnt = 0 
        
        return max(maxcnt, cnt)  


        