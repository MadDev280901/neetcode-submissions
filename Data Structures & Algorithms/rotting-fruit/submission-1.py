import collections
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0
        
        # Step 1: Initialize the queue and count fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 2: Multi-source BFS level by level
        while q and fresh > 0:
            # Process exactly the number of rotten fruits at the current minute
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    
                    # If in bounds and fresh, rot it
                    if (0 <= row < ROWS and 
                        0 <= col < COLS and 
                        grid[row][col] == 1):
                        
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            # Increment time after processing the whole level
            time += 1
            
        # Step 3: Check if any fresh fruits survived
        if fresh == 0:
            return time
        return -1