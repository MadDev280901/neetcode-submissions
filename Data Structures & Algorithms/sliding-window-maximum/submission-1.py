class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx = -float('inf')
        for i in range(k):
            mx = max(mx, nums[i])
        
        res = [0]*(len(nums)-k+1)
        res[0] = mx
        
        for i in range(1, len(nums)-k+1):
            leaving = nums[i-1]
            entering = nums[i+k-1]
            
            if leaving == mx:
                # FIX: Reset mx before recalculating for the new window
                mx = -float('inf') 
                for j in range(i, i+k):
                    mx = max(mx, nums[j])
            else:
                if entering >= mx:
                    mx = max(mx, entering)
            
            res[i] = mx
            
        return res