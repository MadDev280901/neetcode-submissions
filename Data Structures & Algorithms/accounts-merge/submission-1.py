from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n: int):
        # Using arrays (lists) is much faster than dicts for dense integer nodes
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        # Iterative path halving: Faster constant time in Python than recursion
        while i != self.parent[i]:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i == root_j:
            return False
            
        # Union by rank: Attach smaller tree to the root of the larger tree
        if self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        elif self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_acc = {}
        
        # 1. Map emails to account indices and union connected accounts
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_acc:
                    uf.union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i
                    
        # 2. Group emails by their unified root account leader
        root_to_emails = defaultdict(list)
        for email, i in email_to_acc.items():
            root = uf.find(i)
            root_to_emails[root].append(email)
            
        # 3. Construct the final output array
        res = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            # Sorting at the end ensures we only sort the final merged list once
            res.append([name] + sorted(emails))
            
        return res