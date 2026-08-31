class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return False
        class UnionFind:
            def __init__(self, n):
                self.par = [i for i in range(n)]
                self.rank = [1 for i in range(n)]
            
            def find(self, x):
                while x != self.par[x]:
                    self.par[x] = self.par[self.par[x]]
                    x = self.par[x]
                
                return x
            
            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return False 
                if self.rank[root_x] == self.rank[root_y]:
                    self.par[root_y] = root_x
                    self.rank[root_x] += 1
                elif self.rank[root_x] > self.rank[root_y]:
                    self.par[root_y] = root_x
                else:
                    self.par[root_x] = root_y
                
                return True

        tree = UnionFind(n)
        for edge in edges:
            x, y = edge[0], edge[1]
            if not tree.union(x, y):
                return False 
        
        return True 
        