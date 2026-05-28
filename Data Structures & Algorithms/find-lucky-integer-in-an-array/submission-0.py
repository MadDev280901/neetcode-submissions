class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {i:0 for i in arr}
        for num in arr:
            freq[num]+=1
        
        ans = []
        for num in freq:
            if num == freq[num]:
                ans.append(num)
        
        if ans:
            return max(ans)
        else: 
            return -1
        