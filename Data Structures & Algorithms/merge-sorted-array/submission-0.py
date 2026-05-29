class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l, r, k = m-1, n-1, m+n-1
        while l >= 0 and r >= 0 and k >= 0:
            u, v = nums1[l], nums2[r]
            if u > v:
                nums1[l], nums1[k] = nums1[k], nums1[l]
                k-=1
                l-=1
            
            else:
                nums2[r], nums1[k] = nums1[k], nums2[r]
                k-=1
                r-=1
        
        while r >= 0 and k >= 0:

            nums2[r], nums1[k] = nums1[k], nums2[r]
            k-=1
            r-=1

        

        