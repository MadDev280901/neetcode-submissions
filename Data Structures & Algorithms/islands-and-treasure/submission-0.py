from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()

        # 1. Add all treasure cells to the queue.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # 2. Standard BFS directions: down, up, right, left.
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # 3. Expand outward from all treasures simultaneously.
        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Ignore out-of-bounds cells.
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue

                # Ignore water and already-filled cells.
                if grid[nr][nc] != INF:
                    continue

                # Since BFS expands level by level,
                # this is the shortest distance to a treasure.
                grid[nr][nc] = grid[r][c] + 1

                q.append((nr, nc))