class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[n-1] - arr[0]) // n

        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] == arr[0] + mid * diff:
                lo = mid + 1        # no missing on left, search right
            else:
                hi = mid            # missing is at or before mid
        return arr[0] + lo * diff