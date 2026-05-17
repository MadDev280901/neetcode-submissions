class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        if self.stack: 
            q = self.stack.pop()
            self.minstack.pop()
            return q 
        return False 
        

    def top(self) -> int:
        if self.stack: 
            q = self.stack[-1]
            return q 
        return False 
        
    def getMin(self) -> int:
        if self.stack: 
            q = self.minstack[-1]
            return q 
        return False 
        
