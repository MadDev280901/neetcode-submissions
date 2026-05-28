class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        N = n * n

        seen = set()
        repeated = -1
        total = 0

        for row in grid:
            for x in row:
                total += x

                if x in seen:
                    repeated = x
                else:
                    seen.add(x)

        expected = N * (N + 1) // 2

        missing = expected - (total - repeated)

        return [repeated, missing]