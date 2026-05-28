class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        seen = [0]*n
        for i in nums:
            if not seen[i-1]:
                seen[i-1] = 1

        ans = []
        for i, e in enumerate(seen):
            if e == 0:
                ans.append(i+1)        

        return ans