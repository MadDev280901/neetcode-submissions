class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_cnt, close_cnt, path):
            # Base case: valid combination found when both counts reach n
            if open_cnt == n and close_cnt == n:
                res.append("".join(path))
                return
            
            # Decision 1: Add an open parenthesis if we haven't used all 'n' of them
            if open_cnt < n:
                path.append("(")
                backtrack(open_cnt + 1, close_cnt, path)
                path.pop()
                
            # Decision 2: Add a closed parenthesis ONLY if it matches an existing open one
            if close_cnt < open_cnt:
                path.append(")")
                backtrack(open_cnt, close_cnt + 1, path)
                path.pop()
                
        backtrack(0, 0, [])
        return res