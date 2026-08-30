class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows, cols = len(triangle), len(triangle[-1])
        memo = collections.defaultdict(int)
        def f(r, c):
            if r == rows:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            
            memo[(r, c)] = triangle[r][c] + min(f(r+1, c), f(r+1, c+1))
            return memo[(r, c)]

        return f(0, 0)

        