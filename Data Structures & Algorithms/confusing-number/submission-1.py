class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        original = n
        rotated = 0

        while n:
            digit = n % 10
            n //= 10

            if digit not in rotate:
                return False

            rotated = rotated * 10 + rotate[digit]

        return rotated != original
        