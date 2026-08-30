class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def f(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            else: 
                memo[i] = min(cost[i] + f(i+1), cost[i] + f(i+2))
                return memo[i]
        
        return min(f(0), f(1))
        