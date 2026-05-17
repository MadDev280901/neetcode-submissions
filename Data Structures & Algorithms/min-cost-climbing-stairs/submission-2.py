class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=2: 
            return min(cost)

        else: 
            a, b = cost[-1], 0
            for i in range(len(cost)-2, -1, -1):
                a, b = min(a, b)+cost[i], a

            return min(a, b)
        