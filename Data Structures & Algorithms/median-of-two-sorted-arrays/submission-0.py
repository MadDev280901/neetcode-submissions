class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always run binary search on the smaller array to minimize the search space
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
            
        total = len(A) + len(B)
        half = total // 2
        
        l, r = 0, len(A)
        
        while True:
            i = l + (r - l) // 2 # Pointer in A
            j = half - i         # Pointer in B
            
            # Get edge values for the partitions, using infinity for out-of-bounds
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")
            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")
            
            # Check if the partition is perfectly valid
            if Aleft <= Bright and Bleft <= Aright:
                # If total length is odd, the right partition has one extra element
                if total % 2 != 0:
                    return float(min(Aright, Bright))
                # If even, take the max of lefts and min of rights
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            # A's left partition is too big, shrink it
            elif Aleft > Bright:
                r = i - 1
            # A's left partition is too small, grow it
            else:
                l = i + 1