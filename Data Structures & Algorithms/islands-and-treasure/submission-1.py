class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find the treasures
        # search outwards from there
        treasure_coords = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasure_coords.add((i, j))
        
        while treasure_coords:
            ti, tj = treasure_coords.pop()
            q = [(ti, tj, 0)]
            visited = set()
            while q:
                i, j, d = q.pop()
                if (i, j) in visited and d >= grid[i][j]:
                    continue
                grid[i][j] = min(d, grid[i][j])
                neighbors = self.getNeighbors(i, j, grid)
                for (x, y) in neighbors:
                    if grid[x][y] == -1:
                        continue
                    if grid[x][y] > d:
                        # grid[x][y] = d
                        q.append((x, y, d+1))
                visited.add((i, j))

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