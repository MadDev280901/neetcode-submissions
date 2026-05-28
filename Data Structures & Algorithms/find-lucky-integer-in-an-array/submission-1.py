class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {i:0 for i in arr}
        for num in arr:
            freq[num]+=1
        
        largest = -float('inf')
        for num in freq:
            if num == freq[num]:
                largest = max(largest, num)
        
        if largest > 0:
            return largest
        return -1
        