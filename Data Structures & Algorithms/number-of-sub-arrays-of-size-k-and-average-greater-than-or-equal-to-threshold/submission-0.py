class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if n <= k:
            return 1 if sum(arr)/n >= threshold else 0 
        
        else: 
            l, r = 0, 0
            curr_sum = 0
            cnt = 0 
            while r < n:
                curr_sum += arr[r]
                if r - l + 1 == k:
                    cnt += 1 if curr_sum / k >= threshold else 0
                    curr_sum -= arr[l]
                    l += 1
                r += 1
            return cnt