class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        region_coords = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    region_coords.add((i, j))
        
        border_coords = set()
        for i in range(len(board)):
            if board[i][0] == "O":
                border_coords.add((i, 0))
            if board[i][len(board[0])-1] == "O":
                border_coords.add((i, len(board[0])-1))
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                border_coords.add((0, i))
            if board[len(board)-1][i] == "O":
                border_coords.add((len(board)-1, i))
        
        visited = set()
        q = list(border_coords)
        while q:
            i, j = q.pop()
            if (i, j) in visited:
                continue
            neighbors = self.getNeighbors(i, j, board)
            for neighbor in neighbors:
                if neighbor in region_coords:
                    q.append(neighbor)
            visited.add((i, j))
        
        # print("visited", visited)
        # print("region coords", region_coords)

        difference = region_coords.difference(visited)
        for x, y in list(difference):
            board[x][y] = 'X'
    
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