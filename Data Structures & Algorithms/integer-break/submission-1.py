class Solution:
    def integerBreak(self, n: int) -> int:
        memo = collections.defaultdict(int)
        def f(i):
            
            if i == 1:
                return 1
            
            if i in memo:
                return memo[i]
            
            tmp = 0 if i == n else i
            
            for j in range(1, i):
                tmp = max(tmp, f(j) * f(i-j))
            
            memo[i] = tmp
            return memo[i]
        return f(n)