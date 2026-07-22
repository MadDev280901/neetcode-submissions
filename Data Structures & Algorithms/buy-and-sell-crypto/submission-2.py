class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        bestProfit = 0 

        for price in prices: 
            if price < minSoFar: 
                minSoFar = price 
            
            bestProfit = max(bestProfit, price - minSoFar)
        
        return bestProfit 


        