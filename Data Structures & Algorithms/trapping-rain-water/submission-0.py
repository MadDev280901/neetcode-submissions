class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        
        # Step 1: Precompute left maximums
        max_left = [0] * n
        max_left[0] = height[0]
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
            
        # Step 2: Precompute right maximums
        max_right = [0] * n
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
            
        # Step 3: Calculate trapped water at each index
        total_water = 0
        for i in range(n):
            water_at_i = min(max_left[i], max_right[i]) - height[i]
            total_water += water_at_i
            
        return total_water