class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        directi = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        perimeter = 0 
        def helper(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return 1
            
            if grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0

            
            visited.add((r, c))

            perimeter = 0 
            for dr, dc in directi:
                if (r+dr, c+dc) not in visited:
                    perimeter += helper(r+dr, c+dc)

            return perimeter

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] and (r, c) not in visited:
                    return helper(r, c)

        
            




            



        