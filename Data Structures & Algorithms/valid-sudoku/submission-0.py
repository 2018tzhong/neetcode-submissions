class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows valid
        for i in range(len(board)):
            if not self.checkRowValid(board, i):
                return False

        # check cols valid
        for j in range(len(board[0])):
            if not self.checkColValid(board, j):
                return False

        # check boxes valid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.checkBoxValid(board, i, j):
                    return False

        return True
        
    def checkRowValid(self, board, rIdx):
        counts = {str(i): 0 for i in range(1, len(board)+1)}
        for i in range(len(board[rIdx])):
            if board[rIdx][i] == ".":
                continue
            if counts[board[rIdx][i]] == 1:
                print("violating board[rIdx][i]", rIdx, i, board[rIdx][i])
                return False
            else:
                counts[board[rIdx][i]] += 1
        return True

    def checkColValid(self, board, cIdx):
        counts = {str(i): 0 for i in range(1, len(board)+1)}
        for j in range(len(board)):
            if board[j][cIdx] == ".":
                continue
            if counts[board[j][cIdx]] == 1:
                print("violating board[j][cIdx]", j, cIdx, board[j][cIdx])
                return False
            else:
                counts[board[j][cIdx]] += 1
        return True 

    def checkBoxValid(self, board, rIdx, cIdx):
        counts = {str(i): 0 for i in range(1, len(board)+1)}
        for i in range(rIdx, rIdx + 3):
            for j in range(cIdx, cIdx+3):
                if board[i][j] == ".":
                    continue
                if counts[board[i][j]] == 1:
                    print("violating board[i][j]", i, j, board[i][j])
                    return False
                else:
                    counts[board[i][j]] += 1
        return True