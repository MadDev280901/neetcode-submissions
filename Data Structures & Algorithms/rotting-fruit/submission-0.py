from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        # initialize queue with all rotten fruits
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        # no fresh fruit initially
        if fresh == 0:
            return 0

        time = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q and fresh > 0:

            # one BFS layer = one minute
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < m and
                        0 <= nc < n and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            time += 1

        return time if fresh == 0 else -1