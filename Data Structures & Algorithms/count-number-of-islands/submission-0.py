class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find all 1s
        land_coords = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    land_coords.add((i, j))
        # print(land_coords)
        # account for them
        islands = 0
        while land_coords:
            curr = land_coords.pop()
            islands += 1
            q = [curr]
            visited = set()
            while q:
                i, j = q.pop()
                if (i, j) in visited:
                    continue
                neighbors = self.getNeighbors(i, j, grid)
                for (x, y) in neighbors:
                    if grid[x][y] == "1":
                        land_coords.discard((x, y))
                        q.append((x, y))
                visited.add((i, j))
            # print("after looping", land_coords)

        return islands

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