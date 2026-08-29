class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freqMap = collections.defaultdict(int)
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        count_arr = [[] for _ in range(len(nums)+1)]
        for num in freqMap.keys(): 
            count_arr[freqMap[num]].append(num)
        
        for i in range(len(nums), -1, -1):
            if len(count_arr[i]) == 0:
                continue
            
            else: 
                for elem in count_arr[i]:
                    if k > 0:
                        res.append(elem)
                        k-=1
                    else: 
                        return res
            
        return res

            


        