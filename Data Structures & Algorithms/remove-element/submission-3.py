class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        toCopy = 0 
        for num in nums: 
            if num == val: 
                continue 
            else: 
                nums[toCopy] = num
                toCopy+=1

        return toCopy
