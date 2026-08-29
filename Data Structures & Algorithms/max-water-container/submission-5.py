class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mx = -float('inf')
        l, r = 0, len(heights)-1

        while l < r:
            currArea = (r-l)*min(heights[l], heights[r])
            mx = max(mx, currArea)

            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1
        
        return mx if mx != -float('inf') else 0 


        