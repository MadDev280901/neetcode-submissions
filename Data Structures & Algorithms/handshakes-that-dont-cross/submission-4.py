class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        def numShakesMemo(n, memo):
            if n == 0: 
                return 1 
            if n == 2: 
                return 1 
            if n == 4: 
                return 2

            else: 
                if n in memo: 
                    return memo[n]
                
                memo[n] = 0 
                for k in range(0,n, 2): 
                    memo[n] += numShakesMemo(k, memo) * numShakesMemo(n-2-k, memo)

                return memo[n]
        return numShakesMemo(numPeople, {}) % (10**9 + 7)
        