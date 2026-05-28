class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = [0]*1001
        for i in nums1:
            if not table[i]:
                table[i]+=1
        
        for j in nums2:
            if table[j] == 1:
                table[j]+=1
        
        ans = []
        for i, num in enumerate(table):
            if num == 2:
                ans.append(i)
        
        return ans


        