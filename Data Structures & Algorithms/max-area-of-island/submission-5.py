class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # vis = set()

        def helper(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            # if (r, c) in vis:
            #    return 

            # vis.add((r, c))
            grid[r][c] = 0
            return 1 + helper(r, c+1) + helper(r, c-1) + helper(r+1, c) + helper(r-1, c)
        
        maxArea = 0 
        for r in range(m): 
            for c in range(n): 
                if grid[r][c] == 1:
                    maxArea = max(maxArea, helper(r, c))
        
        return maxArea
        
        