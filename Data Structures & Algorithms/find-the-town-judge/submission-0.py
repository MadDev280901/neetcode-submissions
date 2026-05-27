class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegree = [0]*n
        outdegree = [0]*n

        for edge in trust:
            u, v = edge[0], edge[1]
            indegree[v-1] += 1
            outdegree[u-1] += 1
        
        for vertex in range(n):
            if indegree[vertex] == (n-1) and outdegree[vertex] == 0:
                return vertex+1
        
        return -1