class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(start, current_target, path):
            if current_target == 0:
                res.append(path.copy())
                return
            if current_target < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the exact same level of the recursive tree
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Optimization: Since the array is sorted, if the current number 
                # exceeds the target, all subsequent numbers will too.
                if candidates[i] > current_target:
                    break

                path.append(candidates[i])
                
                # Move to i + 1 because we can only use each element once
                backtrack(i + 1, current_target - candidates[i], path)
                
                path.pop()

        backtrack(0, target, [])
        return res