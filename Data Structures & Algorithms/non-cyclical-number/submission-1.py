class Solution:
    def isHappy(self, n: int) -> bool:
        def digi_sum(x):
            total = 0
            while x:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total

        seen = set()

        while True:
            if n == 1:
                return True

            if n in seen:
                return False

            seen.add(n)
            n = digi_sum(n)