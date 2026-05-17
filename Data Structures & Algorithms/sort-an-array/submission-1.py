class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using Merge Sort with optimized space complexity.
        
        Time Complexity: O(n log n) - We divide the array in half log(n) times, 
                         and merge takes linear time.
        Space Complexity: O(n) - We use a single auxiliary array 'temp' of size n, 
                          plus O(log n) for the recursion stack. This is better 
                          than O(n log n) space used by slicing-heavy implementations.
        """
        if not nums:
            return nums
            
        # Pre-allocate a temporary array to reuse during merging.
        # This prevents the overhead of creating thousands of small list objects.
        temp = [0] * len(nums)
        
        self._merge_sort(nums, 0, len(nums) - 1, temp)
        return nums

    def _merge_sort(self, nums: List[int], left: int, right: int, temp: List[int]):
        # Base case: single element or invalid range
        if left >= right:
            return

        mid = (left + right) // 2

        # Recursively sort the left and right halves
        self._merge_sort(nums, left, mid, temp)
        self._merge_sort(nums, mid + 1, right, temp)

        # Optimization: If the largest element of the left half is smaller than
        # the smallest element of the right half, they are already sorted.
        if nums[mid] <= nums[mid + 1]:
            return

        # Merge the two sorted halves
        self._merge(nums, left, mid, right, temp)

    def _merge(self, nums: List[int], left: int, mid: int, right: int, temp: List[int]):
        i = left        # Pointer for left half
        j = mid + 1     # Pointer for right half
        k = left        # Pointer for temp array

        # Compare elements from both halves and place the smaller one into temp
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left half
        # (Remaining elements from the right half are structurally already in place
        # in the original array if we were merging back directly, but here we 
        # ensure temp is complete or just copy the necessary parts back.)
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
            
        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1

        # Copy the sorted portion from temp back to the original array.
        # Python's slice assignment is implemented in C and is highly efficient.
        nums[left:right + 1] = temp[left:right + 1]