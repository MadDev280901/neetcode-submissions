class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : x[0])

        memo = collections.defaultdict(int)
        def f(i):
            if i == len(envelopes):
                return 0
            
            if i in memo:
                return memo[i]

            h0, w0 = envelopes[i][0], envelopes[i][1]
            ans = 1

            for j in range(len(envelopes) - 1, i, -1):
                h, w = envelopes[j][0], envelopes[j][1]
                if h > h0 and w > w0:
                    ans = max(ans, 1 + f(j))
                
            memo[i] = ans
            return memo[i]
        
        return max(f(i) for i in range(len(envelopes)))


        