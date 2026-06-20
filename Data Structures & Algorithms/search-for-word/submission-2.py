class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        q = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    q.append((word[0], i, j, set([(i, j)])))
        # print(q)
        while q:
            curr, i, j, path = q.pop(0)
            if len(curr) == len(word):
                if curr == word:
                    return True
                continue
            next_letter = word[len(curr)]
            next_coords = self.getEligibleSteps(i, j, board)
            # print(curr, path, next_coords)
            for coord in next_coords:
                if board[coord[0]][coord[1]] == next_letter and not coord in path:
                    new_path = path.copy()
                    new_path.add((coord[0], coord[1]))
                    q.append((curr+next_letter, coord[0], coord[1], new_path))
            # todo: handle repeats of coordinates    
        return False 
    
    def getEligibleSteps(self, i, j, board):
        # curr_path_set = set(curr_path)
        coords = []
        if i > 0:
            coords.append((i-1, j))
        if j > 0:
            coords.append((i, j-1))
        if i < len(board)-1:
            coords.append((i+1, j))
        if j < len(board[0])-1:
            coords.append((i, j+1))
        return coords