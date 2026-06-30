class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        look = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            look[c].append(n)

        res = []
        for i in range(len(look)-1, 0, -1):
            for n in look[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        

        

        



        