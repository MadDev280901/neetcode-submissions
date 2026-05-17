class Solution:
    def tribonacciMemo(self, n, memo):
        if n <= 1: return n 
        if n == 2: return 1
        else: 
            if n in memo: 
                return memo[n]
            
            left = self.tribonacciMemo(n-3, memo)
            middle = self.tribonacciMemo(n-2, memo)
            right = self.tribonacciMemo(n-1, memo)

            memo[n] = left + middle + right
            return memo[n]

    def tribonacci(self, n: int) -> int:
        return self.tribonacciMemo(n, {})
        