class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x < 10:
            return True

        m = 1
        while x // m >= 10:
            m *= 10

        while x:
            first = x // m
            last = x % 10

            if first != last:
                return False

            x = (x % m) // 10
            m //= 100

        return True