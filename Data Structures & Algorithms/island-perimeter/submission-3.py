class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        m, n = len(grid), len(grid[0])

        def helper(r, c):
            if r < 0 or r >= m or c < 0 or c>= n or grid[r][c] == 0:
                return 1
            
            if (r, c) in vis:
                return 0
            
            
            vis.add((r, c))

            perimeter = 0 
            perimeter += helper(r, c+1)
            perimeter += helper(r-1, c)
            perimeter += helper(r, c-1)
            perimeter += helper(r+1, c)

            return perimeter
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    return helper(r, c)
        
        return 0 


        