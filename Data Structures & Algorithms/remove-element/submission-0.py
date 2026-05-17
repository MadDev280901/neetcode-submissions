class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k, i, r = 0, 0 , len(nums)-1
        while i <= r: 
            if nums[i] == val: 
                nums[i], nums[r] = nums[r], nums[i]
                r-=1
            else:
                i+=1 
                k+=1

            print(nums)
                
        print(nums)
        return k 


        