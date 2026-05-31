class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n
        
        l, r = 0, n
        while l <= r:
            m = (l+r)//2
            q = (m**2 + m)//2

            if q <= n:
                l = m+1
            else:
                r = m-1
        
        return r
