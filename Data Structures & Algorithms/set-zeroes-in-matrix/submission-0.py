class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        col_count = [1 for i in range(len(matrix[0]))]
        row_count = [1 for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col_count[j] = 0
                    row_count[i] = 0
        
        for i, val in enumerate(col_count):
            if val == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        for i, val in enumerate(row_count):
            if val == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        