class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        return self.find(self.parents[x])

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        rx, ry = self.rank[x], self.rank[y]
        if px == py:
            return False
        if rx < ry:
            py, px = px, py
        self.parents[py] = self.parents[px]
        if rx == ry:
            self.rank[x] += 1
    
    def numComponents(self):
        counter = 0
        for i in range(len(self.parents)):
            if i == self.parents[i]:
                counter += 1
        return counter

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = UnionFind(n)
        for i, j in edges:
            ds.union(i, j)
        return ds.numComponents()
