class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = nums[:]

        for i in range(1, len(self.prefixSum)):
            self.prefixSum[i] = self.prefixSum[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left > right:
            return -1

        if left == 0:
            return self.prefixSum[right]

        return self.prefixSum[right] - self.prefixSum[left - 1]