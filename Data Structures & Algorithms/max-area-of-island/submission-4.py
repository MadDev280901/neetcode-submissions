class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        maxArea = 0
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    area = 0
                    stack = [(r, c)]
                    grid[r][c] = 0 # Mark as visited immediately
                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        area += 1
                        
                        # Inline checks are faster than iterating through a directions array
                        if curr_r > 0 and grid[curr_r-1][curr_c] == 1:
                            grid[curr_r-1][curr_c] = 0
                            stack.append((curr_r-1, curr_c))
                        if curr_r + 1 < m and grid[curr_r+1][curr_c] == 1:
                            grid[curr_r+1][curr_c] = 0
                            stack.append((curr_r+1, curr_c))
                        if curr_c > 0 and grid[curr_r][curr_c-1] == 1:
                            grid[curr_r][curr_c-1] = 0
                            stack.append((curr_r, curr_c-1))
                        if curr_c + 1 < n and grid[curr_r][curr_c+1] == 1:
                            grid[curr_r][curr_c+1] = 0
                            stack.append((curr_r, curr_c+1))
                            
                    # Avoid the built-in max() function overhead
                    if area > maxArea:
                        maxArea = area
                        
        return maxArea