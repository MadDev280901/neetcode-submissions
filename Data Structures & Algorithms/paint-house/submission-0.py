class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        memo = {}

        def dfs(i, color):
            """
            min cost to paint houses 0..i
            with house i painted as 'color'
            """

            if i == 0:
                return costs[0][color]

            if (i, color) in memo:
                return memo[(i, color)]

            ans = costs[i][color] + min(
                dfs(i - 1, prev)
                for prev in range(3)
                if prev != color
            )

            memo[(i, color)] = ans
            return ans

        return min(dfs(n - 1, c) for c in range(3))