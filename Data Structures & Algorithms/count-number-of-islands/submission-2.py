class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        vis = set()

        def helper(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
                return
            
            if (r, c) in vis:
               return 

            vis.add((r, c))
            helper(r, c+1)
            helper(r, c-1)
            helper(r+1, c)
            helper(r-1, c)

            return 
        
        cntIslands = 0 
        for r in range(m): 
            for c in range(n): 
                if (r, c) not in vis and grid[r][c] == "1":
                    helper(r, c)
                    cntIslands+=1
        
        return cntIslands
        