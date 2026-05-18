class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        n = len(costs)
        memo = {}

        def f(i, last):

            # minimum cost for houses 0..i
            # with house i painted 'last'

            if i == 0:
                return costs[0][last]

            if (i, last) in memo:
                return memo[(i, last)]

            ans = float('inf')

            for prev in range(3):

                if prev != last:
                    ans = min(
                        ans,
                        costs[i][last] + f(i - 1, prev)
                    )

            memo[(i, last)] = ans
            return ans

        return min(
            f(n - 1, color)
            for color in range(3)
        )