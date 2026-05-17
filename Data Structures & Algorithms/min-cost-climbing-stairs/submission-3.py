class Solution:
    def minCostClimbingStairsMemo(self, i, cost, memo): 
        if i <= 1: 
            return 0
        else: 
            if i in memo: 
                return memo[i]
            
            left = cost[i-2] + self.minCostClimbingStairsMemo(i-2, cost, memo)
            right = cost[i-1] + self.minCostClimbingStairsMemo(i-1, cost, memo)
            
            memo[i] = min(left, right)
            return memo[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        return self.minCostClimbingStairsMemo(len(cost), cost, {})
        