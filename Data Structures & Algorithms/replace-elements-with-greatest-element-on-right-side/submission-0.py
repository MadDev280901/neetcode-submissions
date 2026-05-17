class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr = [0]*len(arr)
        max_before = -1 
        for i in range(len(arr)-1, -1, -1):
            new_arr[i] = max_before
            max_before = max(max_before, arr[i])
        return new_arr
            


        