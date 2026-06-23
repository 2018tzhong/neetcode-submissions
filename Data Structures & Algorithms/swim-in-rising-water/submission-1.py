class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        q = [(grid[0][0], 0, 0)]
        max_el_so_far = math.inf
        visited = set()
        while q:
            max_elevation, x, y  = heapq.heappop(q)
            if x == len(grid)-1 and y == len(grid[0])-1:
                max_el_so_far = min(max_elevation, max_el_so_far)
                continue
            if max_elevation >= max_el_so_far:
                continue
            if (x, y) in visited:
                continue
            visited.add((x, y))
            neighbors = self.getNeighbors(x, y, grid)
            for x2, y2 in neighbors:
                if not (x2, y2) in visited:
                    heapq.heappush(q, (max(max_elevation, grid[x2][y2]), x2, y2))
            # print(q)
        if max_el_so_far == math.inf:
            return 0
        return max_el_so_far 

    def getNeighbors(self, x, y, grid):
        neighbors = []
        if x > 0:
            neighbors.append((x-1, y))
        if y > 0:
            neighbors.append((x, y-1))
        if x < len(grid) - 1:
            neighbors.append((x+1, y))
        if y < len(grid[0]) - 1:
            neighbors.append((x, y+1))
        return neighbors