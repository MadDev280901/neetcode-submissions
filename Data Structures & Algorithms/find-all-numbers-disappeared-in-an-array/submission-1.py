class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            curr = abs(nums[i])
            nums[curr - 1] = -abs(nums[curr - 1])

        ans = []

        for i, e in enumerate(nums):
            if e > 0:
                ans.append(i + 1)

        return ans