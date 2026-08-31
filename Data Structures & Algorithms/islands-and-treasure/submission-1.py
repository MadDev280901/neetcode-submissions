from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        # Add all treasure chests to the queue as our starting points
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        # Define the 4 possible directions (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Perform multi-source BFS
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                row, col = r + dr, c + dc
                
                # Check bounds and if the cell is an unvisited land cell (INF)
                if (row < 0 or row >= ROWS or 
                    col < 0 or col >= COLS or 
                    grid[row][col] != 2147483647):
                    continue
                
                # The distance is the current cell's distance + 1
                grid[row][col] = grid[r][c] + 1
                q.append((row, col))