class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', '{':'}', '[':']'}
        
        for char in s: 
            if char in brackets.keys(): 
                stack.append(char)
            else: 
                if not stack: 
                    return False 
                elif brackets[stack[-1]] == char: 
                    stack.pop()
                else: 
                    return False 

        return True if not stack else False