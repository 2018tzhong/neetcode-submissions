class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_coords = set()
        rotten_coords = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_coords.add((i, j))
                if grid[i][j] == 2:
                    rotten_coords.add((i, j))
        
        turns = 0
        last_rotten = 0
        while fresh_coords:
            # start from rotten_coords, move outward.
            layer = list(rotten_coords)
            q = []
            neighbors = []
            for (i, j) in layer:
                neighbors.extend(self.getNeighbors(i, j, grid))
            for (x, y) in neighbors:
                if (x, y) in fresh_coords:
                    fresh_coords.discard((x, y))
                    rotten_coords.add((x, y))
            turns += 1
            if len(rotten_coords) == last_rotten:
                break
            last_rotten = len(rotten_coords)
        
        if fresh_coords:
            return -1
        return turns

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