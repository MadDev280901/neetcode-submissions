class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # Tracks visited coordinates in the current DFS path

        def dfs(r, c, i):
            # Base case 1: We found all characters in the word
            if i == len(word):
                return True
            
            # Base case 2: Out of bounds, character mismatch, or cell already visited
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False
            
            # Mark the current cell as visited
            path.add((r, c))
            
            # Explore all 4 adjacent neighbors
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            
            # Backtrack: remove the current cell from the path so it can be used in other branches
            path.remove((r, c))
            return res

        # Start the DFS from every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): 
                    return True
                    
        return False