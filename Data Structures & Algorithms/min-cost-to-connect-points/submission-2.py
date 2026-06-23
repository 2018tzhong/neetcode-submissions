import heapq

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
            px, py = py, px
        self.parents[py] = px
        if rx == ry:
            self.rank[x] += 1
        return True 
    
    def checkOneSet(self):
        count = 0
        for idx in range(len(self.parents)):
            if self.parents[idx] == idx:
                count += 1
        return count == 1

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # mst for kruskals
        heap = []
        for idx1 in range(len(points)):
            for idx2 in range(idx1+1, len(points)):
                i1, j1 = points[idx1]
                i2, j2 = points[idx2]
                cost = self.calcCost(i1, j1, i2, j2)
                heapq.heappush(heap, (cost, idx1, idx2))
        # print(heap)
        total_cost = 0
        uf = UnionFind(len(points))
        joined = set()
        while heap:
            cost, u, v = heapq.heappop(heap)
            if uf.union(u, v):
                total_cost += cost
                joined.add(u)
                joined.add(v)
            if uf.checkOneSet():
                return total_cost
        return 0

    def calcCost(self, x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)