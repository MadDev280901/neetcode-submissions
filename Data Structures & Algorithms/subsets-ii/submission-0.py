class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort to group duplicates
        res = []
        subset = []

        def backtrack(i):
            # Step 2: Base case - if index reaches the end, append a COPY of the subset
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # Step 3: Include the current number
            subset.append(nums[i])
            backtrack(i + 1)
            subset.pop()
            
            # Step 4: Exclude the current number and skip all duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # Start the recursion from the next unique number
            backtrack(i + 1)
            
        backtrack(0)
        return res