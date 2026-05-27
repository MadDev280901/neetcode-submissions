class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(i, j, m, n):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            
            if grid[i][j] == 0:
                return 0

            if (i, j) in visited:
                return 0

            visited.add((i, j))
            return 1 + dfs(i, j-1, m, n) + dfs(i-1, j, m, n) + dfs(i+1, j, m, n) + dfs(i, j+1, m, n)

        
        maxi = -float('inf')
        for i in range(m): 
            for j in range(n): 
                if (i, j) not in visited and grid[i][j]:
                    maxi = max(maxi, dfs(i, j, m, n))

        return maxi if maxi > 0 else 0
        