class Solution:
    def trap(self, heights: List[int]) -> int:
        lMax = [0] * len(heights)
        rMax = [0] * len(heights)
        for i in range(0, len(heights)):
            if i == 0:
                lMax[i] = heights[i]
            else:
                lMax[i] = max(lMax[i-1], heights[i])
        
        for i in range(len(heights)-1, -1, -1):
            if i == len(heights)-1:
                rMax[i] = heights[i]
            else:
                rMax[i] = max(heights[i], rMax[i+1])
        
        ans = 0 
        for i in range(len(heights)):
            ans += min(lMax[i], rMax[i]) - heights[i]

        return ans
        