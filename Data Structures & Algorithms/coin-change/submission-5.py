class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = collections.defaultdict(int)
        def f(target):
            if target == 0:
                return 0
            if target < min(coins):
                return float('inf')
            
            if target in memo:
                return memo[target]

            else:
                ans = float('inf')
                for coin in coins:
                    if coin <= target:
                        ans = min(ans, 1+f(target-coin))
                
                memo[target] = ans
                return memo[target]
        
        ans = f(amount)
        if amount > 0: 
            return ans if ans != float('inf') else -1
        
        return ans 
            
                

                


        