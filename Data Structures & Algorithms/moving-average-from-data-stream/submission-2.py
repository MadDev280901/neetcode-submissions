from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size 
        self.nums = deque()
        self.sums = 0 
        

    def next(self, val: int) -> float:
        
        if len(self.nums) == self.size:
            self.sums -= self.nums.popleft()
            self.nums.append(val)
            self.sums+= val

            return self.sums/self.size
        
        else:
            self.nums.append(val)
            self.sums += val
            return self.sums/len(self.nums)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
