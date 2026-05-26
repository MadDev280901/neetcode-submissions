class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(r, c):

            # bounds check
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # water
            if grid[r][c] == "0":
                return

            # already visited
            if (r, c) in visited:
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)

        return islands