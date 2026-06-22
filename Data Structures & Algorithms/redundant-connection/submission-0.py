class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
        self.lastCycleEdge = None
    
    def find(self, x):
        if x == self.parents[x]:
            return x
        return self.find(self.parents[x])
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        rx, ry = self.rank[x], self.rank[y]
        if px == py:
            self.lastCycleEdge = [x, y]
        if rx < ry:
            px, py = py, px
        self.parents[py] = px
        if rx == ry:
            self.rank[x] += 1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        ds = UnionFind(n)
        for i, j in edges:
            ds.union(i, j)
        return ds.lastCycleEdge