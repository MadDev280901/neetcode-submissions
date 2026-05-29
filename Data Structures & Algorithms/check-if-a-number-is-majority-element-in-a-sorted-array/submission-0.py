class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0 
        for i in nums:
            if i == target:
                cnt+=1
            else:
                cnt-=1
        
        if cnt>0: return True
        return False
        