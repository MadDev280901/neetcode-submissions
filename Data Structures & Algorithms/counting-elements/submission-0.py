class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique = set(arr)
        cnt = 0 
        for num in arr:
            if num+1 in unique:
                cnt+=1

        return cnt
        