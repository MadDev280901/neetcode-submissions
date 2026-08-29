class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxAfter = -float('inf')
        maxProfit = -float('inf')
        for i in range(len(prices)-1, -1, -1):
            maxProfit = max(maxProfit, mxAfter-prices[i])
            mxAfter = max(mxAfter, prices[i])

        return maxProfit if maxProfit > 0 else 0          