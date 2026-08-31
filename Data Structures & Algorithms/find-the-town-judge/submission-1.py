class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = {i:0 for i in range(n)}
        outdegree = {i:0 for i in range(n)}

        for rel in trust:
            a, b = rel[0], rel[1]
            indegree[b-1] += 1
            outdegree[a-1] += 1
        
        for i in range(n): 
            if indegree[i] == (n-1) and outdegree[i] == 0:
                return i+1
        
        return -1

        