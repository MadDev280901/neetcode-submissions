class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        memo = collections.defaultdict(int)
        def f(i, color):
            if i >= len(costs):
                return 0
            
            if (i, color) in memo:
                return memo[(i, color)]
            
            else: 
                tmp = float('inf')
                for c in range(3):
                    if c != color:
                        tmp = min(tmp, costs[i][c] + f(i+1, c))
                
                memo[(i, color)] = tmp 
                return memo[(i, color)]
        
        return f(0, None)
