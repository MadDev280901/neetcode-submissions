class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(r: int, c: int) -> int:
            # Water or out-of-bounds contributes one edge to perimeter
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 1
            if grid[r][c] == 0:
                return 1

            # Already-counted land contributes nothing new
            if (r, c) in visited:
                return 0

            visited.add((r, c))

            perimeter = 0
            perimeter += dfs(r + 1, c)
            perimeter += dfs(r - 1, c)
            perimeter += dfs(r, c + 1)
            perimeter += dfs(r, c - 1)

            return perimeter

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0