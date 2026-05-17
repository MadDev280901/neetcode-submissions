class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {'(':')', '[': ']', '{':'}'}
        
        for char in s: 
            if char in matches.keys(): 
                stack.append(char)
            else: 
                if not stack: 
                    return False 
                else: 
                    top_char = stack[-1]
                    if matches[top_char] == char: 
                        stack.pop()
                    else: 
                        return False 
        
        if not stack: 
            return True 
            
        return False