class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            tmp = curr_max

            if curr_max < arr[i]:
                curr_max = arr[i]
                arr[i] = tmp 
            
            else:
                arr[i] = curr_max

        arr[-1] = -1
        return arr
        