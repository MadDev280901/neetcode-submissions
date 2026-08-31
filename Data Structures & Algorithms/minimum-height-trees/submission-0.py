import collections
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Edge cases: 1 or 2 nodes
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]
            
        # Build adjacency list and degree array
        adj = collections.defaultdict(list)
        degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        # Initialize queue with all initial leaves (nodes with exactly 1 edge)
        leaves = collections.deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)
                
        # Trim the leaves layer by layer
        remaining_nodes = n
        while remaining_nodes > 2:
            # Number of leaves in the current layer
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            # Process all leaves at the current level
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                
                # Remove the edge and update the neighbor's degree
                for neighbor in adj[leaf]:
                    degree[neighbor] -= 1
                    # If the neighbor becomes a leaf, add it to the queue for the next layer
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
                        
        # The remaining nodes (1 or 2) are the centroids / roots for minimum height
        return list(leaves)