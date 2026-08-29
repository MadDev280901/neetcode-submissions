class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path):
            # Base case: if the permutation is complete, add a copy to results
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for num in nums:
                # If the number is already in our current path, skip it
                if num in path:
                    continue
                
                # Choose the number
                path.append(num)
                # Explore further
                backtrack(path)
                # Backtrack: remove the number to try the next one
                path.pop()
                
        backtrack([])
        return res