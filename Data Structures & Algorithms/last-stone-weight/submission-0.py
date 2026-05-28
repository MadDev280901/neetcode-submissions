from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        l = len(stones)
        while l: 
            if l == 1:
                return stones[0]
            
            x, y = heappop_max(stones), heappop_max(stones)
            if x > y:
                heappush_max(stones, x-y)
                l-=1
            
            elif x < y:
                heappush_max(stones, y-x)
                l-=1
            
            else:
                l-=2

        return 0 
            

        