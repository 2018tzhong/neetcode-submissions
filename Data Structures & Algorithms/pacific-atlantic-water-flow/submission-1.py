class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific_set = set()
        atlantic_set = set()

        pq = []
        aq = []
        for i in range(len(heights)):
            pq.append((i, 0))
            aq.append((i, len(heights[0])-1))
        for i in range(len(heights[0])):
            pq.append((0, i))
            aq.append((len(heights)-1, i))


        visited = set()
        q = pq
        while q:
            i, j= q.pop()
            if (i, j) in visited:
                continue
            neighbors = self.getNeighbors(i, j, heights)
            for (x, y) in neighbors:
                if heights[x][y] >= heights[i][j]:
                    q.append((x, y))
            visited.add((i, j))
            pacific_set.add((i, j))
        
        q = aq
        visited = set()
        while q:
            i, j= q.pop()
            if (i, j) in visited:
                continue
            neighbors = self.getNeighbors(i, j, heights)
            for (x, y) in neighbors:
                if heights[x][y] >= heights[i][j]:
                    q.append((x, y))
            visited.add((i, j))
            atlantic_set.add((i, j))

        return [list(i) for i in list(atlantic_set.intersection(pacific_set))]

        
    def getNeighbors(self, i, j, grid):
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if i < len(grid) - 1:
            neighbors.append((i+1, j))
        if j < len(grid[0]) - 1:
            neighbors.append((i, j+1))
        return neighbors