import math
import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)
        for _ in range(k):
            x = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, math.floor(math.sqrt(x)))

        return sum(gifts)
        