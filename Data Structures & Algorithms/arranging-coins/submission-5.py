class Solution:
    def arrangeCoins(self, n: int) -> int:
        q = math.sqrt(1 + 8*n)
        return math.floor((q-1)/2)
