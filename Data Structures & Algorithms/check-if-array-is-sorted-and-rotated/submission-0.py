class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_order = sorted(nums)

        for k in range(len(nums)):
            isSorted = True
            for i in range(len(nums)):
                if nums[(i+k)%len(nums)] == sorted_order[i]:
                    continue
                else: 
                    isSorted = False
                    break
            
            if isSorted:
                return True
        
        return False
            


        