import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()  # Stores indices
        
        for i, num in enumerate(nums):
            # 1. Remove elements that are no longer in the window
            if q and q[0] < i - k + 1:
                q.popleft()
            
            # 2. Remove smaller elements from the back (maintain decreasing order)
            while q and nums[q[-1]] < num:
                q.pop()
            
            # 3. Add the current element's index
            q.append(i)
            
            # 4. Record the max once the first window is completely formed
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res