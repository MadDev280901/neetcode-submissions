class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # --- PASS 1: Move all 0s to the front ---
        i = 0
        zeroEnd = 0  # This tracks where the next 0 should go
        
        while i < len(nums):
            if nums[i] == 0:
                nums[i], nums[zeroEnd] = nums[zeroEnd], nums[i]
                zeroEnd += 1
                i += 1  # Crucial: Always move to the next element after processing
            else:
                i += 1
        
        # At this point, nums[:zeroEnd] are all 0s.
        # We start the second pass from zeroEnd, because 
        # everything before that is already sorted (0s).

        # --- PASS 2: Move all 1s to the front of the remaining portion ---
        i = zeroEnd
        # We can reuse the same pointer variable, but let's call it 
        # 'oneEnd' mentally. It starts where the 0s ended.
        
        while i < len(nums):
            if nums[i] == 1:
                nums[i], nums[zeroEnd] = nums[zeroEnd], nums[i]
                zeroEnd += 1
                i += 1
            else:
                i += 1