class MovingAverage:

    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.count = 0
        self.idx = 0
        self.total = 0

    def next(self, val):

        self.total -= self.arr[self.idx]
        self.arr[self.idx] = val
        self.total += val

        self.idx = (self.idx + 1) % self.size
        self.count = min(self.count + 1, self.size)

        return self.total / self.count