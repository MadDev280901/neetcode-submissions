class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def count_in_range(nums, target, lo, hi):
            count = 0
            for i in range(lo, hi + 1):
                if nums[i] == target:
                    count += 1
            return count

        def recurse(lo, hi):
            # Base Case: An array of size 1 has exactly 1 majority element
            if lo == hi:
                return nums[lo]

            mid = (lo + hi) // 2

            # Recurse on left and right halves
            left_majority = recurse(lo, mid)
            right_majority = recurse(mid + 1, hi)

            # If halves agree, return that element
            if left_majority == right_majority:
                return left_majority

            # If they disagree, count which candidate is dominant in the current range
            left_count = count_in_range(nums, left_majority, lo, hi)
            right_count = count_in_range(nums, right_majority, lo, hi)

            return left_majority if left_count > right_count else right_majority

        return recurse(0, len(nums) - 1)
            