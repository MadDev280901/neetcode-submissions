class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # start, end = 0, len(nums)-1
        # while start < end:
        #     if nums[start] == 0: 
        #         nums[start], nums[end] = nums[end], nums[start]
        #         end-=1
        #     else: 
        #         start+=1
        write = 0 
        for read in range(len(nums)): 
            if nums[read] != 0: 
                nums[write] = nums[read]
                write += 1

        for i in range(write, len(nums)): 
            nums[i] = 0 
        
        return nums
        



        