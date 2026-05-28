class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.summation = 0
        self.deque = deque()

    def next(self, val: int) -> float:
        self.deque.append(val)
        self.summation += val
        if len(self.deque) > self.size:
            self.summation -= self.deque.popleft()
        
        return self.summation / len(self.deque)
 

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
